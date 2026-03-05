import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("Advertising.csv")

X = data[['TV','Radio','Newspaper']]
y = data['Sales']

model = LinearRegression()

model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully")

import matplotlib.pyplot as plt


plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")
plt.title("Advertising vs Sales")

