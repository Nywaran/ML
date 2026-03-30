from flask import Flask, render_template, request
import LinealRegression
import LogisticRegressionModel
import RidgeClassifierModel

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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


@app.route('/linear-regression/concepts')
def lr_concepts():
    return render_template('linear_regression/concepts.html')

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


@app.route('/logistic-regression/concepts')
def log_concepts():
    return render_template('logistic_regression/concepts.html')

@app.route('/logistic-regression/application', methods=['GET', 'POST'])
def log_application():
    prediction = None
    probability = None
    if request.method == 'POST':
        age              = float(request.form['age'])
        income           = float(request.form['income'])
        loan_amount      = float(request.form['loan_amount'])
        credit_score     = float(request.form['credit_score'])
        months_employed  = float(request.form['months_employed'])
        num_credit_lines = float(request.form['num_credit_lines'])
        interest_rate    = float(request.form['interest_rate'])
        loan_term        = float(request.form['loan_term'])
        dti_ratio        = float(request.form['dti_ratio'])
        prediction, probability = LogisticRegressionModel.predict( age, income, loan_amount, credit_score, months_employed, num_credit_lines, interest_rate, loan_term, dti_ratio
        )
    return render_template('logistic_regression/application.html', prediction=prediction, probability=probability, metrics=LogisticRegressionModel.metrics)

@app.route('/ridge-classifier/concepts')
def rc_concepts():
    return render_template('ridge_classifier/concepts.html')

@app.route('/ridge-classifier/application', methods=['GET', 'POST'])
def rc_application():
    prediction = None
    probability = None
    if request.method == 'POST':
        age              = float(request.form['age'])
        income           = float(request.form['income'])
        loan_amount      = float(request.form['loan_amount'])
        credit_score     = float(request.form['credit_score'])
        months_employed  = float(request.form['months_employed'])
        num_credit_lines = float(request.form['num_credit_lines'])
        interest_rate    = float(request.form['interest_rate'])
        loan_term        = float(request.form['loan_term'])
        dti_ratio        = float(request.form['dti_ratio'])
        prediction, probability = RidgeClassifierModel.predict( age, income, loan_amount, credit_score, months_employed, num_credit_lines, interest_rate, loan_term, dti_ratio
        )
    return render_template('ridge_classifier/application.html', prediction=prediction, probability=probability, metrics=RidgeClassifierModel.metrics)