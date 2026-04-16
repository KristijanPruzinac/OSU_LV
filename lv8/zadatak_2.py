import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from keras.models import load_model

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

model = load_model("model.keras")

predictions = np.argmax(model.predict(x_test), axis=1)

wrong_indices = np.where(predictions != y_test)[0]

plt.figure()
for i in range(min(9, len(wrong_indices))):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_test[wrong_indices[i]])
    plt.title("Predicted: {}, Actual: {}".format(
        predictions[wrong_indices[i]], y_test[wrong_indices[i]]))
plt.tight_layout(pad=1.5)
plt.show()
