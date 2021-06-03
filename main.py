from flask import Flask, request
from models.Preprocess import predict_image
import cv2, numpy as np
import tensorflow as tf 
from keras.models import load_model
# from models.Preprocess import RequestToImage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

model = load_model('model_ml_vg_1.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # ini logic buat ambil gambar udah ini tugas gua
    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    return predict_image(img,model)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')

