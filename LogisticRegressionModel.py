import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc)

df = pd.read_csv('Loan_default.csv')

le = LabelEncoder()
cat_cols = ['Education', 'EmploymentType', 'MaritalStatus', 'LoanPurpose','HasMortgage', 'HasDependents', 'HasCoSigner']
for col in cat_cols: df[col] = le.fit_transform(df[col])

X = df.drop(columns=['LoanID', 'Default'])
y = df['Default']
feature_cols = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

model = LogisticRegression(random_state=42, max_iter=500, class_weight='balanced')
model.fit(X_train_sc, y_train)

y_pred = model.predict(X_test_sc)
y_prob = model.predict_proba(X_test_sc)[:, 1]

metrics = {
    'accuracy': round(accuracy_score(y_test, y_pred) * 100, 2),
    'precision': round(precision_score(y_test, y_pred) * 100, 2),
    'recall': round(recall_score(y_test, y_pred) * 100, 2),
    'f1': round(f1_score(y_test, y_pred) * 100, 2),
}

def predict(age, income, loan_amount, credit_score, months_employed,
            num_credit_lines, interest_rate, loan_term, dti_ratio):
    client = pd.DataFrame([[age, income, loan_amount, credit_score, months_employed, num_credit_lines, interest_rate, loan_term, dti_ratio, 0, 0, 0, 0, 0, 0, 0]], columns=feature_cols)
    client_sc = scaler.transform(client)
    result = model.predict(client_sc)[0]
    prob = model.predict_proba(client_sc)[0]
    return int(result), round(float(prob[1]) * 100, 1)