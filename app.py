from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/szolgaltatasok')
def szolgaltatasok():
    return render_template('szolgaltatasok.html')

@app.route('/foglalas', methods=['GET', 'POST'])
def foglalas():
    if request.method == 'POST':
        return redirect(url_for('foglalas_sikeres'))
    return render_template('foglalas.html')

@app.route('/foglalas/sikeres')
def foglalas_sikeres():
    return render_template('foglalas_sikeres.html')

@app.route('/webshop')
def webshop():
    # Demó terméklista
    termekek = [
        {'nev': "HANK'S Parfüm #1", 'ar': '6 990 Ft', 'kep': 'parfum1.jpg'},
        {'nev': "HANK'S Hajlakk Ultra", 'ar': '4 290 Ft', 'kep': 'hajlakk.jpg'},
        {'nev': "Szakállbalzsam Deluxe", 'ar': '3 590 Ft', 'kep': 'balzsam.jpg'},
        {'nev': "Férfi sampon – Fresh", 'ar': '2 990 Ft', 'kep': 'sampon.jpg'},
        {'nev': "Vágóolló Pro", 'ar': '9 990 Ft', 'kep': 'ollo.jpg'},
        {'nev': "Hajformázó paszta Strong", 'ar': '3 990 Ft', 'kep': 'paszta.jpg'},
        {'nev': "Szakállolaj Classic", 'ar': '4 490 Ft', 'kep': 'olaj.jpg'},
        {'nev': "HANK’S Fodrász kötény", 'ar': '6 990 Ft', 'kep': 'koteny.jpg'},
        {'nev': "Hajszárító Slim", 'ar': '11 990 Ft', 'kep': 'hajszarito.jpg'},
        {'nev': "Ajándékcsomag Premium", 'ar': '14 990 Ft', 'kep': 'ajandek.jpg'}
    ]
    return render_template('webshop.html', termekek=termekek)

@app.route('/kosar', methods=['GET', 'POST'])
def kosar():
    if request.method == 'POST':
        return redirect(url_for('sikeres_rendeles'))
    return render_template('kosar.html')

@app.route('/sikeres-rendeles')
def sikeres_rendeles():
    return render_template('sikeres_rendeles.html')

@app.route('/kapcsolat')
def kapcsolat():
    return render_template('kapcsolat.html')

if __name__ == '__main__':
    app.run(debug=True)
