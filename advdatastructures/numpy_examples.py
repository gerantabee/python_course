from random import randrange

import numpy as np
import random as rand

# Numpy arrays outperform native arrays in a few ways, including speed
# They contain native mathematical methods that would normally require manual or external intervention
# They can contain only one data type

grades = np.array([55, 65, 75, 80, 91, 62, 50, 70])

# Dot notation works for most functions, except median(?)
print("Mean:",grades.mean())
print("Max:",grades.max())
print("Min:",grades.min())
print("Standard Deviation:",grades.std())
print("Median:",np.median(grades))

print(grades[1])
print(grades[2:4])
print(grades[:3]) # Stops at 3, doesn't INCLUDE 3
print(grades[-2:])

# expenses = np.loadtxt('../data/expense_reports.csv', delimiter=',', dtype=str)
expenses = np.genfromtxt('../data/expense_reports.csv', delimiter=',', skip_header=1,dtype=None)
print("Shape of array:",expenses.shape) # The shape (size) of our data
print(expenses)
transpose_exp = np.transpose(expenses)
print("Shape of transposed array:",transpose_exp.shape)

expenses_dollars = expenses[:, 3]
for i,x in enumerate(expenses_dollars):
    newx = x.replace("$","")
    expenses_dollars[i] = int(newx)


exp = expenses_dollars.astype(int, order='K', casting='unsafe', subok=True, copy=True)#

print(exp)
print("Total expense average", round(exp.mean(),2))
