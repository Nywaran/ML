from flask import Flask, render_template, request
import json
import LinealRegression
import LogisticRegressionModel
import RidgeClassifierModel
import Clustering

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
        prediction = LinealRegression.predict(
            float(request.form['open']), float(request.form['high']),
            float(request.form['low']), float(request.form['volume'])
        )
    return render_template('linear_regression/application.html', prediction=prediction)


@app.route('/logistic-regression/concepts')
def log_concepts():
    return render_template('logistic_regression/concepts.html')

@app.route('/logistic-regression/application', methods=['GET', 'POST'])
def log_application():
    prediction = probability = None
    if request.method == 'POST':
        prediction, probability = LogisticRegressionModel.predict(
            float(request.form['age']), float(request.form['income']),
            float(request.form['loan_amount']), float(request.form['credit_score']),
            float(request.form['months_employed']), float(request.form['num_credit_lines']),
            float(request.form['interest_rate']), float(request.form['loan_term']),
            float(request.form['dti_ratio'])
        )
    return render_template('logistic_regression/application.html',
                           prediction=prediction, probability=probability,
                           metrics=LogisticRegressionModel.metrics)


@app.route('/ridge-classifier/concepts')
def rc_concepts():
    return render_template('ridge_classifier/concepts.html')

@app.route('/ridge-classifier/application', methods=['GET', 'POST'])
def rc_application():
    prediction = probability = None
    if request.method == 'POST':
        prediction, probability = RidgeClassifierModel.predict(
            float(request.form['age']), float(request.form['income']),
            float(request.form['loan_amount']), float(request.form['credit_score']),
            float(request.form['months_employed']), float(request.form['num_credit_lines']),
            float(request.form['interest_rate']), float(request.form['loan_term']),
            float(request.form['dti_ratio'])
        )
    return render_template('ridge_classifier/application.html',
                           prediction=prediction, probability=probability,
                           metrics=RidgeClassifierModel.metrics)


@app.route('/clustering')
def clustering():
    data = Clustering.applyClustering()
    return render_template('clustering/index.html',
                           result=data['result'],
                           clusterSummary=data['clusterSummary'],
                           centers=data['centers'])


@app.route('/unsupervised/concepts')
def unsupervised_concepts():
    return render_template('unsupervised/concepts.html')

@app.route('/unsupervised/manual')
def unsupervised_manual():
    with open('iterations_data.json', 'r') as f:
        iterations = json.load(f)
    return render_template('unsupervised/manual.html', iterations=iterations)

@app.route('/unsupervised/application')
def unsupervised_application():
    with open('app_data.json', 'r') as f:
        data = json.load(f)
    return render_template('unsupervised/application.html',
                           summary=data['summary'],
                           centroids=data['centroids'],
                           table_data=data['table_data'])

if __name__ == '__main__':
    app.run(debug=True)