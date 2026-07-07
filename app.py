from flask import Flask, render_template, request
import numpy as np
import pickle
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

FEATURE_COLUMNS = [
    'CODE_GENDER',
    'FLAG_OWN_CAR',
    'FLAG_OWN_REALTY',
    'CNT_CHILDREN',
    'AMT_INCOME_TOTAL',
    'NAME_INCOME_TYPE',
    'NAME_EDUCATION_TYPE',
    'NAME_FAMILY_STATUS',
    'NAME_HOUSING_TYPE',
    'DAYS_BIRTH',
    'DAYS_EMPLOYED',
    'OCCUPATION_TYPE'
]


def build_model():
    data = pd.DataFrame([
        [1, 1, 1, 1, 350000, 2, 0, 1, 2, -14000, -4000, 0, 1],
        [1, 1, 1, 0, 300000, 2, 0, 1, 2, -12000, -2000, 2, 1],
        [0, 1, 1, 0, 260000, 2, 0, 1, 2, -15000, -3000, 1, 1],
        [1, 0, 0, 4, 40000, 0, 2, 0, 0, -22000, -18000, 4, 0],
        [1, 0, 0, 3, 30000, 0, 1, 0, 0, -25000, -10000, 3, 0],
        [0, 0, 0, 2, 50000, 1, 1, 2, 1, -20000, -4000, 4, 0],
        [1, 1, 1, 2, 220000, 2, 0, 1, 2, -13000, -5000, 0, 1],
        [0, 0, 0, 5, 20000, 0, 2, 0, 0, -24000, -20000, 4, 0],
    ], columns=FEATURE_COLUMNS + ['target'])

    X = data[FEATURE_COLUMNS]
    y = data['target']

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=4000)
    )
    model.fit(X, y)
    return model


model = build_model()
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(col, 0)) for col in FEATURE_COLUMNS]
    except (ValueError, TypeError):
        return "Error: Invalid input values. Please enter valid numbers.", 400

    final_input = np.array(features).reshape(1, -1)

    try:
        prediction = int(model.predict(final_input)[0])
    except ValueError as e:
        return f"Prediction error: {str(e)}", 400

    result = "Credit Card Approved" if prediction == 1 else "Credit Card Rejected"
    return render_template('result.html', prediction_text=result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
