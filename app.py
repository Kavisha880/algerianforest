from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('regressor.pkl', 'rb'))

UPLOAD_FOLDER = 'static/uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Load and preprocess the uploaded CSV file
    df = pd.read_csv(filepath)

    # Optional: Drop non-numeric or unwanted columns if needed
    if 'day' in df.columns:
        df.drop(['day'], axis=1, inplace=True)

    # Predict FWI using your trained model
    prediction = model.predict(df)

    # Return prediction(s) to user
    result = f"Predicted FWI Values: {prediction.tolist()}"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
