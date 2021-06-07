from flask import Flask, request
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

def predict_image(image_uplo, model):
    im = image_uplo
    im_array = np.asarray(im)
    im_array = im_array * (1 / 255)
    predict_label = np.argmax(model.predict(im_array))

    if predict_label == 0:
        return ('covid')
    elif predict_label == 1:
        return ('normal')
    elif predict_label == 2:
        return ('penumonia')


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

@app.route('/predict', methods=['POST'])
def predict():
    # Load Model
    model = tf.keras.models.load_model('model_ml_vg_1.h5')

    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))

    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img = np.vstack([x])

    return predict_image(img, model)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')

