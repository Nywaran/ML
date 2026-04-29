# Machine Learning — Flask Web Application

A web application built with Flask that presents four Machine Learning use cases and implements supervised and unsupervised learning modules with real datasets and interactive prediction forms.

---

## Project Structure

```
Machine Learning/
│
├── app.py
├── LinealRegression.py
├── LogisticRegressionModel.py
├── RidgeClassifierModel.py
├── Clustering.py
├── UnsupervisedModel.py
├── gold_futures_timeseries.csv
├── Loan_default.csv
├── manual_dataset.csv
├── iterations_data.json
├── app_data.json
├── requirements.txt
├── Procfile
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── regresion_grafica.png
│       ├── lr_confusion_matrix.png
│       ├── lr_roc_curve.png
│       ├── rc_confusion_matrix.png
│       ├── rc_roc_curve.png
│       ├── kmeans_iter1.png
│       ├── kmeans_iter2.png
│       ├── kmeans_iter3.png
│       ├── variance_plot.png
│       └── app_clusters.png
│
└── templates/
    ├── layout.html
    ├── index.html
    ├── includes/
    │   ├── header.html
    │   └── footer.html
    ├── use_cases/
    │   ├── health.html
    │   ├── finance.html
    │   ├── cybersecurity.html
    │   └── education.html
    ├── linear_regression/
    │   ├── concepts.html
    │   └── application.html
    ├── logistic_regression/
    │   ├── concepts.html
    │   └── application.html
    ├── ridge_classifier/
    │   ├── concepts.html
    │   └── application.html
    ├── clustering/
    │   └── index.html
    └── unsupervised/
        ├── concepts.html
        ├── manual.html
        └── application.html
```

---

## Features

- **Home** — Introduction to Machine Learning with four use cases
- **ML Use Cases** — Health, Finance, Cybersecurity, Education
- **Supervised ML**
  - Linear Regression — Gold futures closing price prediction
  - Logistic Regression — Loan default prediction
  - Ridge Classifier — Loan default prediction with L2 regularization
- **Unsupervised ML**
  - Basic Concepts — K-Means theory and definitions
  - K-Means Manual Exercise — 3 iterations with distance tables and scatter plots
  - Clustering Application — Customer segmentation with 1,000 records
- **Clustering** — K-Means demo with 12 customer profiles

---

## Datasets

| Dataset | Records | Use |
|---------|---------|-----|
| Gold Futures Time Series | 1,169 | Linear Regression |
| Loan Default | 255,347 | Logistic Regression / Ridge Classifier |
| Student Study Hours | 100 | K-Means Manual Exercise |
| Customer Segmentation | 1,000 | Clustering Application |

---

## Execution Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Nywaran/ML.git
cd ML
```

### 2. Create and activate virtual environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## Navigation

| Route | Description |
|-------|-------------|
| `/` | Home |
| `/use-cases/health` | Health use case |
| `/use-cases/finance` | Finance use case |
| `/use-cases/cybersecurity` | Cybersecurity use case |
| `/use-cases/education` | Education use case |
| `/linear-regression/concepts` | Linear Regression concepts |
| `/linear-regression/application` | Linear Regression prediction form |
| `/logistic-regression/concepts` | Logistic Regression concepts |
| `/logistic-regression/application` | Logistic Regression prediction form |
| `/ridge-classifier/concepts` | Ridge Classifier concepts |
| `/ridge-classifier/application` | Ridge Classifier prediction form |
| `/unsupervised/concepts` | Unsupervised Learning concepts |
| `/unsupervised/manual` | K-Means manual exercise |
| `/unsupervised/application` | Customer clustering application |
| `/clustering` | K-Means demo |

---

## Technologies

- Python 3
- Flask
- pandas
- scikit-learn
- matplotlib
- seaborn
- gunicorn
- HTML / CSS

---

## Branches

| Branch | Content |
|--------|---------|
| `main` | Production-ready code |
| `linear-regression` | Linear regression module |
| `logistic-regression` | Logistic regression module |
| `ridge-classifier` | Ridge classifier module |
| `unsupervised-learning` | K-Means clustering module |
| `clustering` | Clustering demo |
| `deploy-settings` | Render deployment configuration |

---

## Live Application

Deployed on Render: https://ml-byv5.onrender.com/

---

## Author

Julian Sanchez - Universidad de Cundinamarca.