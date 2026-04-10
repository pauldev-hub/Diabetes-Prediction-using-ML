from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # allow React frontend to call this API

# Load trained model - use correct path relative to this file
model_path = os.path.join(os.path.dirname(__file__), "diabetes_model.pkl")
model = joblib.load(model_path)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Diabetes Prediction API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from React
        data = request.get_json()

        # Convert input into numpy array
        features = np.array([[
            data["pregnancies"],
            data["glucose"],
            data["bloodPressure"],
            data["skinThickness"],
            data["insulin"],
            data["bmi"],
            data["dpf"],   # Diabetes Pedigree Function
            data["age"]
        ]], dtype=float)

        # Make prediction
        prediction = int(model.predict(features)[0])
        probability = float(model.predict_proba(features)[0][1] * 100)

        # Return result
        return jsonify({
            "prediction": prediction,   # 0 = No Diabetes, 1 = Diabetes
            "probability": round(probability, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # Run locally (Render will override this with Gunicorn)
    app.run(host="0.0.0.0", port=5000, debug=True)
