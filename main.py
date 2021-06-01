from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

@app.route('/predict', methods=['POST'])
def predict():
    return "Hasil Predict"

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')