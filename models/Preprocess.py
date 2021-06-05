import numpy as np

# ini logic udah benar tapi mungkin masih perlu perbaikan (karena ini belom tau bisa/engga) kalo engga harus diperbaiki
def predict_label(img_path):
    i = 

    predict_array = model.predict(im_input)[0]

    predict_label = np.argmax(model.predict(im_input))
    return predict_label
