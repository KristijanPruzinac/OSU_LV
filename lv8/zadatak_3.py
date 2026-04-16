import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from matplotlib.image import imread
from keras.models import load_model

model = load_model("model.keras")

image1 = np.expand_dims(255 - imread("number1.png")[:, :, 0] * 255, axis=0)
image2 = np.expand_dims(255 - imread("number2.png")[:, :, 0] * 255, axis=0)

prediction1 = model.predict(image1)
prediction2 = model.predict(image2)

plt.figure()
plt.imshow(image1[0])
plt.title("Predicted: {}".format(np.argmax(prediction1, axis=1)[0]))
plt.show()

plt.figure()
plt.imshow(image2[0])
plt.title("Predicted: {}".format(np.argmax(prediction2, axis=1)[0]))
plt.show()
