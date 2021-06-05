import numpy as np

# ini logic udah benar tapi mungkin masih perlu perbaikan (karena ini belom tau bisa/engga) kalo engga harus diperbaiki
def predict_label(img2):
    i = image.load_img(img2, target-size = (224,224))
    i = iamge.img_to_array(i)/255.0
    i = i.reshape(1,224,224,3)
    p = model.predict_classes(i)
    return dict[p[0]]
