import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
 
data = pd.read_csv('gold_futures_timeseries.csv')
 
X = data[['open', 'high', 'low', 'volume']]
y = data['close']
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
 
model = LinearRegression()
model.fit(X_train_scaled, y_train)
 
def predict(open_price, high, low, volume):
    client = pd.DataFrame([[open_price, high, low, volume]],
                          columns=['open', 'high', 'low', 'volume'])
    client_scaled = scaler.transform(client)
    result = model.predict(client_scaled)[0]
    return round(float(result), 2)