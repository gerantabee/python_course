import csv
import pandas as pd

# Create a dictionary
states_income = {}
with open('../data/state_average_income.csv', 'r') as f:
    for key, val in csv.reader(f):
        states_income[key] = int(val)

# Series creates a one dimensional structure, similar to a dictionary but more efficient
states_income_ser = pd.Series(states_income)
print(states_income_ser)

print(states_income_ser.mean(numeric_only=True))

# We can use methods like argmax and argmin to get the position of highest/lowest values
maxstate = states_income_ser.argmax()
minstate = states_income_ser.argmin()
keymax = states_income_ser.index[maxstate]
keymin = states_income_ser.index[minstate]

print("The state with the highest average income:", keymax)
print("The state with the lowest average income:", keymin)
