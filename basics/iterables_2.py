from collections import Counter
import csv

#Counters do a tally of uniques from a list of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

departments = []

with open('../data/expense_reports.csv', 'r') as file:
    # reader = csv.reader(file)
    # DictReader maps each element to a dictionary and uses header row as keys
    for i in csv.DictReader(file):
        departments.append(i['Department'])
        # print(i['Department'])

# Gives a tally of departments!
dept = Counter(departments)
print(dept)