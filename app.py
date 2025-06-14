from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'titkoskulcs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# --- MODELL ---
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    service = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

# --- FŐOLDAL (foglalási űrlap) ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        service = request.form["service"]
        dt = request.form["datetime"]

        # ellenőrzés: időpont már foglalt?
        existing = Appointment.query.filter_by(datetime=dt).first()
        if existing:
            flash("Ez az időpont már foglalt, kérlek válassz másikat!")
            return redirect("/")

        appt = Appointment(
            name=name,
            email=email,
            phone=phone,
            service=service,
            datetime=datetime.strptime(dt, "%Y-%m-%dT%H:%M")
        )
        db.session.add(appt)
        db.session.commit()
        return render_template("success.html", name=name)
    
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
