import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

#load dataset
iris = load_iris(as_frame=True)
df = iris.frame
print(df.head())
print(df.info())
print(df.isna().sum())


df.loc[0:10, 'sepal length (cm)'] = np.nan
# Simple strategy: fill missing values with column mean
df.fillna(df.mean(), inplace=True)
x = df.drop(columns='target')
y = df['target']


plt.figure()
plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    y
)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width")
plt.show()




print(x)
print(y)
print(df.head())
print(df.tail())


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)



plt.figure()
plt.imshow(confusion_matrix(y_test, y_pred))
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.colorbar()
plt.show()


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


plt.figure()
plt.bar(["Logistic Regression"], [accuracy])
plt.ylim(0, 1)
plt.title("Model Accuracy")
plt.show()




