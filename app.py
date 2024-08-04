from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

HUGGING_FACE_API_URL = "https://sakibrumu-food-image-classification.hf.space/run/predict?__theme=light"
HUGGING_FACE_API_TOKEN = "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"

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    files = {'file': (image.filename, image.read(), image.content_type)}

    headers = {
        'Authorization': f'Bearer {HUGGING_FACE_API_TOKEN}',
    }

    response = requests.post(HUGGING_FACE_API_URL, files=files, headers=headers)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to get prediction'}), 500

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
