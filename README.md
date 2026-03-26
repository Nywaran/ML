# Machine Learning — Flask Web Application

A web application built with Flask that presents four Machine Learning use cases and a supervised learning module focused on Linear Regression applied to gold futures price prediction.

---

## Project Structure

```
Machine Learning/
│
├── app.py
├── LinealRegression.py
├── gold_futures_timeseries.csv
├── requirements.txt
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── regresion_grafica.png
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
    └── linear_regression/
        ├── concepts.html
        └── application.html
```

---

## Features

- **Home** — Introduction to machine learning with an overview of the four use cases
- **ML Use Cases** — Four detailed pages covering health, finance, cybersecurity and education
- **Linear Regression — Basic Concepts** — Explanation of key concepts such as variables, regression line, slope, and intercept
- **Linear Regression — Application** — Real dataset, regression graph, and interactive prediction form for gold futures closing price

---

## Dataset

- **Gold Futures Time Series** — 1,169 daily records from 2021 to 2024
- Source: https://www.kaggle.com
- Variables used: opening price, highest price, lowest price, trading volume
- Target variable: closing price (USD)

---

## Execution Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Nywaran/ML.git
cd ML
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## Navigation

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/use-cases/health` | Health use case |
| `/use-cases/finance` | Finance use case |
| `/use-cases/cybersecurity` | Cybersecurity use case |
| `/use-cases/education` | Education use case |
| `/linear-regression/concepts` | Linear Regression concepts |
| `/linear-regression/application` | Linear Regression application and prediction form |

---

## Technologies Used

- Python 3
- Flask
- pandas
- scikit-learn
- matplotlib
- seaborn
- HTML / CSS

---

## Author

Carlos Julian Sanchez Gonzalez — Universidad de Cundinamarca 2026
