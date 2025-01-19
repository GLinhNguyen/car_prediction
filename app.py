from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# load the trained pipeline
model = joblib.load(r"E:\General Project\Car\car_prediction\random_forest_pipeline.pkl")

@app.route('/')
def home():
    return jsonify({"API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        required_features = ['brand', 'type', 'fuel', 'color', 'gearbox', 'origin', 
                             'mileage_v2', 'seats', 'age']
        for feature in required_features:
            if feature not in data:
                return jsonify({"error": e}), 400
        
        input_data = pd.DataFrame([data])
        
        prediction = model.predict(input_data)[0]
        
        return jsonify({"predicted_price": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
