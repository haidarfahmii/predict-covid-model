from flask import Flask, request
from models.Preprocess import predict_image
import cv2, numpy as np
# from models.Preprocess import RequestToImage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

@app.route('/predict', methods=['POST'])
def predict():
    # ini logic buat ambil gambar udah ini tugas gua
    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    model = tf.load('model.tflite') #ini logic yg dikasih temen gua untuk load model cmn masih belom bener kalian harus
                                    #cari syntax benernya

    return predict_image(img, model)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')

