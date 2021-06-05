import numpy as np

# ini logic udah benar tapi mungkin masih perlu perbaikan (karena ini belom tau bisa/engga) kalo engga harus diperbaiki
def predict_image(image_uplo, model):
    im = image_uplo
    im_array = np.asarray(im)
    im_array = im_array * (1 / 255)
    im_input = tf.reshape(im_array, shape=[1, 224, 224, 3])

    predict_array = model.predict(im_input)[0]

    predict_label = np.argmax(model.predict(im_input))
    return predict_label
