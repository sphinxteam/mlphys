import scipy as sci

## Check Python Version
import sys

assert sys.version.find('3.6') > -1

## Check numpy
import numpy as np
from math import sqrt

n = 1024
A = np.random.randn(n, n) / sqrt(n)
x = np.random.randn(n)
y = np.dot(A,x)
xhat = np.linalg.solve(A,y)
mse = np.mean((xhat - x)**2)
assert mse < 1e-10

## Check Matplotlib
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
x = np.random.randn(n)
y = 3*x + np.random.randn(n)
plt.plot(x,y,'.b')
plt.show()

## Check Pandas
import pandas as pd

df = pd.DataFrame(
        {'a' : [4, 5, 6],
         'b' : [3, 4, 2],
         'c' : [1, 2, 3]},
        index = [1,2,3])

## Check Scikit-Learn
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
clf = svm.SVC(gamma=0.001, C=100)
clf.fit(iris.data[:-1], iris.target[:-1])
clf.predict(iris.data[-1:])