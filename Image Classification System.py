#code to import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#code to import dataset on which we have to do classification
from sklearn.datasets import load_digits
dataset = load_digits()

#declaring variables
X = dataset.data
y = dataset.target

#picking up random digit and putting it in a new variable
some_digit = X[484]
some_digit_image = some_digit.reshape(8 ,8)

#plotting the digit
plt.imshow(some_digit_image)
plt.show()

#code to import logistic regression family to train the data
from sklearn.linear_model import LogisticRegression
lg = LogisticRegression()
lg.fit(X, y)

#code to import decision tree classifier family to train the data
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(max_depth=17)
dtc.fit(X ,y)

#to predict the score
dtc.score(X, y)
dtc.predict(X[[478, 258, 254,369,222], 0:78])