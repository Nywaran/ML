from flask import Flask, render_template, request
import RegresionLogistica
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/LinearRegression/')
def calculateGrade():
    import LinealRegression
    result = LinealRegression.calculateGrade(10)
    return str(result)
 
@app.route('/LogisticRegression/', methods=['GET', 'POST'])
def logistic():
    if request.method == 'POST':
        edad      = float(request.form['edad'])
        ingreso   = float(request.form['ingreso_mensual'])
        visitas   = float(request.form['visitas_web_mes'])
        tiempo    = float(request.form['tiempo_sitio_min'])
        compras   = float(request.form['compras_previas'])
        descuento = float(request.form['descuento_usado'])
 
        resultado, probabilidad = RegresionLogistica.predecir(
            edad, ingreso, visitas, tiempo, compras, descuento
        )
        return render_template('result.html',
                               resultado=resultado,
                               probabilidad=probabilidad)
    return render_template('logistic.html')
 