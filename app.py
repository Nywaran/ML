# Importacion de librerias
from flask import Flask, render_template, request
import LinealRegression
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

# Llamamos los casos de uso, uno por uno
@app.route('/use-cases/health')
def use_case_health():
    return render_template('use_cases/health.html')
 
@app.route('/use-cases/finance')
def use_case_finance():
    return render_template('use_cases/finance.html')
 
@app.route('/use-cases/cybersecurity')
def use_case_cybersecurity():
    return render_template('use_cases/cybersecurity.html')
 
@app.route('/use-cases/education')
def use_case_education():
    return render_template('use_cases/education.html')
 
# Llamamos a la regresión lineal pero solo los conceptos
@app.route('/linear-regression/concepts')
def lr_concepts():
    return render_template('linear_regression/concepts.html')
 
# Llamamos a la apliacaión de la regresión lineal y el dataset
@app.route('/linear-regression/application', methods=['GET', 'POST'])
def lr_application():
    prediction = None
    if request.method == 'POST':
        open_price = float(request.form['open'])
        high       = float(request.form['high'])
        low        = float(request.form['low'])
        volume     = float(request.form['volume'])
        prediction = LinealRegression.predict(open_price, high, low, volume)
    return render_template('linear_regression/application.html', prediction=prediction)