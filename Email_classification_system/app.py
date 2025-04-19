from flask import Flask, request, jsonify
from utils import find_entities
from models import load_models
import os

app = Flask(__name__)

# Load models
try:
    vectorizer, classifier = load_models()
except Exception as e:
    print(f"Error loading models: {e}")
    print("Please train the models first using models.py")
    vectorizer = None
    classifier = None

@app.route("/classify", methods=["POST"])
def classify():
    if vectorizer is None or classifier is None:
        return jsonify({"error": "Models not loaded. Please train the models first."}), 500

    data = request.json
    email_body = data.get("email_body", "")
    
    # Find and mask entities
    entities, masked_email = find_entities(email_body)
    
    # Predict category
    vectorized = vectorizer.transform([masked_email])
    category = classifier.predict(vectorized)[0]
    
    response = {
        "input_email_body": email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
