import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
 
data = pd.read_csv('dataset_regresion_logistica.csv')
 
X = data.drop('target', axis=1)
y = data['target']
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
 
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
 
def predecir(edad, ingreso, visitas, tiempo, compras, descuento):
    cliente = pd.DataFrame([[edad, ingreso, visitas, tiempo, compras, descuento]],
                           columns=X.columns)
    cliente_scaled = scaler.transform(cliente)
    resultado = model.predict(cliente_scaled)[0]
    probabilidad = model.predict_proba(cliente_scaled)[0]
    return int(resultado), round(float(probabilidad[1]) * 100, 1)