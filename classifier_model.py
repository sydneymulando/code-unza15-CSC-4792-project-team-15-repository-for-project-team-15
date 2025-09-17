from flask import Flask, request, jsonify, render_template_string
import joblib
import fitz  # PyMuPDF

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('naive_bayes_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Article Discipline Predictor</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #ffffff;
      color: #333;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .container {
      background: #fff;
      padding: 2rem;
      border-radius: 15px;
      box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
      width: 100%;
      max-width: 600px;
      animation: fadeIn 1s ease;
    }
    h1 {
      text-align: center;
      color: #e63946;
      margin-bottom: 1.5rem;
      animation: slideDown 1s ease;
    }
    label {
      font-weight: bold;
      display: block;
      margin-top: 1rem;
      color: #333;
    }
    input[type="file"] {
      margin-top: 0.5rem;
    }
    button {
      margin-top: 1.5rem;
      width: 100%;
      padding: 0.9rem;
      font-size: 1.1rem;
      font-weight: bold;
      background-color: #e63946;
      color: #fff;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: transform 0.2s ease, background 0.3s ease;
    }
    button:hover {
      background-color: #c1121f;
      transform: translateY(-3px);
    }
    #result {
      margin-top: 1.5rem;
      font-size: 1.2rem;
      font-weight: bold;
      text-align: center;
      color: #333;
      background: #ffe5e5;
      padding: 1rem;
      border-radius: 10px;
      display: none;
      animation: fadeIn 0.8s ease;
      white-space: pre-wrap;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.95); }
      to { opacity: 1; transform: scale(1); }
    }
    @keyframes slideDown {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Article Discipline Predictor</h1>
    <label for="pdf-file">Upload Article PDF:</label>
    <input type="file" id="pdf-file" accept="application/pdf" />
    <button id="predict-btn">Predict Discipline</button>
    <div id="result"></div>
  </div>
  <script>
    document.getElementById('predict-btn').addEventListener('click', () => {
      const fileInput = document.getElementById('pdf-file');
      const resultDiv = document.getElementById('result');
      resultDiv.style.display = 'none';
      resultDiv.textContent = '';
      if (!fileInput.files.length) {
        resultDiv.textContent = '⚠️ Please upload a PDF file.';
        resultDiv.style.display = 'block';
        return;
      }
      const formData = new FormData();
      formData.append('file', fileInput.files[0]);
      resultDiv.textContent = '⏳ Extracting text and predicting...';
      resultDiv.style.display = 'block';
      fetch('/predict', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        if (data.prediction) {
          let text = `✅ Predicted Discipline: ${data.prediction}`;
          if(data.confidence){
            text += `\n🔹 Confidence: ${data.confidence}`;
          }
          resultDiv.textContent = text;
        } else if (data.error) {
          resultDiv.textContent = '❌ Error: ' + data.error;
        } else {
          resultDiv.textContent = '⚠️ Unexpected error';
        }
      })
      .catch(err => {
        resultDiv.textContent = '❌ Error connecting to prediction service.';
        console.error(err);
      });
    });
  </script>
</body>
</html>
"""

def predict_discipline(text):
    X = vectorizer.transform([text])
    proba = model.predict_proba(X)[0]
    pred_index = proba.argmax()
    confidence = proba[pred_index]
    prediction = model.classes_[pred_index]

    allowed_labels = ['Law', 'Social Sciences']
    if prediction not in allowed_labels:
        prediction = 'Unclassified'

    return prediction, confidence

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not file or not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Please upload a valid PDF file'}), 400

    try:
        pdf_bytes = file.read()
        doc = fitz.open(stream=pdf_bytes, filetype='pdf')

        full_text = ""
        for page in doc:
            full_text += page.get_text()

        prediction, confidence = predict_discipline(full_text)
        return jsonify({
            'prediction': prediction,
            'confidence': f"{confidence * 100:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)