import numpy as np
import tensorflow as tf

images = np.load('./test_image/2.npy')

model = tf.keras.models.load_model('model')
pred = model.predict(images.reshape(-1, 28, 28))
print("The answer is", np.argmax(pred))