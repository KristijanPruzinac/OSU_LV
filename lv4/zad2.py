from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error
from sklearn . preprocessing import OneHotEncoder
import sklearn.linear_model as lm

import pandas as pd

from matplotlib import pyplot as plt

data = pd.read_csv("data_C02_emission.csv")
data = data.dropna()

columns = ['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 
                'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 
                'Fuel Consumption Comb (mpg)']

X = data[columns]
y = data['CO2 Emissions (g/km)']

ohe = OneHotEncoder()
X_encoded = ohe.fit_transform(data[["Fuel Type"]]).data
X = pd.concat([X, pd.DataFrame(X_encoded, columns=["Fuel Type"])], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print(X_train)
print(y_train)

plt.scatter(X_train['Engine Size (L)'], y_train, color='blue', label='Training data')
plt.scatter(X_test['Engine Size (L)'], y_test, color='red', label='Test data')

plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')

plt.title('CO2 Emissions vs Engine Size')
plt.legend()
plt.show()

linearModel = lm.LinearRegression()
linearModel.fit(X_train, y_train)

print(linearModel.coef_)

y_test_p = linearModel.predict(X_test)

y_ind = range(len(y_test_p))
plt.scatter(y_ind, y_test, color='blue', label='Stvarni izlazi')
plt.scatter(y_ind, y_test_p, color='red', label='Procjena')

plt.title('Stvarni izlazi vs procjena')
plt.show()

print(mean_absolute_error(y_test, y_test_p))
print(mean_squared_error(y_test, y_test_p))
print(root_mean_squared_error(y_test, y_test_p))

print(y_test_p.max())
print(X_test.iloc[[y_test_p.argmax()]])