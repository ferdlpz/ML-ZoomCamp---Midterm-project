import pickle

from flask import Flask, request, jsonify
import numpy as np
import xgboost as xgb

model_file = 'model_eta=0.1_max_depth=5_min_child_weight=5.bin'

import os
os.chdir('/Users/fdl/Repos/ML-ZoomCamp---Midterm-project/03 Deployment')
print(os.getcwd())

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('longterm-prediction')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform([customer])
    features = list(dv.get_feature_names_out())
    dtest = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dtest)
    # Probabilidades (aplicando Sigmoide al score)
    probabilidades = 1 / (1 + np.exp(-y_pred)) 

    # Etiquetas (Clase 1 si probabilidad > 0.5)
    long_term = (probabilidades >= 0.5).astype(int)

    result = {
        'purchase_probability': float(probabilidades[0]),
        'long_term_customer': bool(long_term[0])
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
