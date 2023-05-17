
import keras.utils as image
import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model(filepath="potholes.h5")


def predict(name):
    img = image.load_img(name, target_size=(64, 64))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = model.predict(images, batch_size=32)

    if classes[0] > 0:
        return True

    else:
        return False
