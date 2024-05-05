from flask import Flask, render_template, request
import joblib, pandas

# Import your dependencies here (joblib, pandas, CountVectorizer)

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json'

model = joblib.load('mylogisticmodel.joblib')
vectorizer = joblib.load('vectorizer.joblib')

# Custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Custom error handler for other types of errors
@app.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html', error_message=str(error)), 500

# Load the CountVectorizer and trained model
# Load other dependencies (pandas, joblib) and prepare your model here

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get tokenized text from the POST request
            text = request.form['text']
            
            # Transform tokenized text into vectors using the fitted CountVectorizer
            # Make sure vectorizer is loaded and ready for transformation
            text_vectorized = vectorizer.transform([text])

            # Make prediction
            prediction = model.predict(text_vectorized)[0]
            
            # Determine prediction label
            prediction_label = 'IT IS A DISASTER' if prediction == 1 else 'IT IS NOT A DISASTER'

            # Render the prediction template with the result
            return render_template("prediction.html", prediction=prediction_label, text=text)
        except Exception as e:
            # Render error template with error message
            return render_template('error.html', error_message=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
