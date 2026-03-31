import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# A
plt.figure()
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='x')
plt.show()

# B

LogisticRegression_model = LogisticRegression()
LogisticRegression_model.fit(X_train, y_train)

y_test_p = LogisticRegression_model.predict(X_test)

# C
print("Koeficijenti {}".format(LogisticRegression_model.coef_))

x1 = np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100)
x2 = -(LogisticRegression_model.intercept_ + LogisticRegression_model.coef_[0, 0]*x1) / LogisticRegression_model.coef_[0, 1]

plt.figure()
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.plot(x1, x2)
plt.show()

# D

print("Tocnost: ", accuracy_score(y_test, y_test_p))
print("Preciznost: ", precision_score(y_test, y_test_p))
print("Odziv: ", recall_score(y_test, y_test_p))

cm = confusion_matrix(y_test, y_test_p)
print("Matrica zabune: ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.show()

# E

plt.figure()
plt.scatter(X_test[:, 0], X_test[:, 1], c=(y_test==y_test_p), cmap=ListedColormap(['black', 'green']), marker='x')
plt.show()