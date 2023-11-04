from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load models
heart_model = joblib.load("models/model_heart.pkl")

diabetes_model = joblib.load("models/model_diabetes.pkl")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict_heart/", methods=["POST"])
def predict_heart():
    features = [float(i) for i in request.form.values()]
    features = np.array([features])
    prediction = heart_model.predict(features)
    return f"Heart Disease Prediction: {'Positive' if prediction else 'Negative'}"


@app.route("/predict_diabetes/", methods=["POST"])
def predict_diabetes():
    features = [float(i) for i in request.form.values()]
    features = np.array([features])
    prediction = diabetes_model.predict(features)
    return f"Diabetes Prediction: {'Positive' if prediction else 'Negative'}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
