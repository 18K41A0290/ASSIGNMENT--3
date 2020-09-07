# -*- coding: utf-8 -*-
"""ASSIGNMENT---3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ei0juldq4mpaWAuzIsPh3hOrsi0kPUlI

1.	Read mobile dataset using pandas, and preprocess it
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d=pd.read_csv("/content/drive/My Drive/Copy of Copy of mobile_cleaned-1549119762886.csv")
pd.set_option("display.max_rows",None,"display.max_columns",None)
d

d.isnull().sum()

l=list(d.columns)
for n in l :
  m=d[n].mean()
  d[n].fillna(m,inplace=True)
d

d.isnull().sum().sum()

"""2.	Draw correlation graph for mobile price with all attributes."""

p=list(d["price"])
l=list(d.columns)
for n in l :
   c=list(d[n])
   plt.xlabel(n)
   plt.ylabel("price")
   plt.plot(c,p,label=n)
   plt.scatter(c,p)
   plt.legend()
   plt.show()

"""3.	Compute outer product of 2 vectors."""

import numpy as np 

matrix1 = np.array([[1, 0], [0, 1]]) 

matrix2 = np.array([[1, 2], [3, 4]]) 

print("Original 2-D matrix:") 

print(matrix1) 

print(matrix2)

print("Outer Product of the two matrix is:") 

result = np.outer(matrix1, matrix2) 

print(result)

"""4.	Write a NumPy program to compute the condition number of a given matrix."""

import numpy as np

matrix = np.array([[1, 2], [3, 4]])
print("Original matrix: ")
print(matrix)

print("Condition number of the said matrix: ")
result = np.linalg.cond(matrix)
print(result)

"""5.write a numpy program to compute the sum of the diagnol elements of a given array (matrix)"""

d=np.array([[10,8,5],[4,4,9],[3,0,5]])
print("matrix=\n",d)
p=np.trace(d)
print("trace=",p)