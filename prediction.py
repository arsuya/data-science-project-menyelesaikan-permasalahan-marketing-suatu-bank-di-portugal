import pandas as pd
import pickle

# Load model yang sudah dilatih
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Masukkan data yang ingin diprediksi
X_new = pd.DataFrame({
    'age': [56], 
    'job': ['housemaid'], 
    'marital': ['married'], 
    'education': ['basic.4y'], 
    'housing': ['no'], 
    'loan': ['no'], 
    'contact': ['telephone'], 
    'month': ['may'], 
    'day_of_week': ['mon'], 
    'campaign': [1], 
    'previous': [0], 
    'poutcome': ['nonexistent'], 
    'emp.var.rate': [1.1], 
    'cons.price.idx': [93.994], 
    'cons.conf.idx': [-36.4], 
    'euribor3m': [4.857], 
    'nr.employed': [5191.0],
    'is_service_job': [0],
    'contact_rate': [0.0]
})

# Model akan memprediksi
y_pred = model.predict(X_new)

# Mengubah nilai prediksi menjadi label yang diminta
y_pred_label = ['yes' if pred == '1' else 'no' for pred in y_pred]

print("Hasil Prediksi:", y_pred_label)
