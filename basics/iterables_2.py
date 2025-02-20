from collections import Counter
import csv
from typing import Dict, Any

'''
    Dictionaries use key/value pairs to store more complex arrays of information
'''
salestax = {"NY": .0825,
            "NY": .0825,
            "MA": .062,
            "FL": .06,
            "TX": .0625,
            "MN": .06875,
            "CA": .0725}

# print(salestax["NY"])
# salestax.values()
salestax.update({"IL": .07, "MN": .03})
salestax["CA"] = .065
print(salestax)
print(salestax.keys())
print(salestax.values())

for i in salestax:
  if salestax[i] == 0:
    print("zero")
  else:
    print(i, ":", salestax[i])

for i,j in salestax:
# for i,j in salestax.items():
    print(i, j)


states = ["NY","IL","MA","CA","TX","TX","OR"]
cities = ["New York","Chicago","Boston", "Los Angeles", "Dallas", "Austin", "Portland"]

city_state: dict = {}

# Unite the lists using enumerate
for index,city in enumerate(cities):
    # city_state[city] = states[index]
    city_state.update({city:states[index]})

city_state.update({"Seattle":"WA"})
city_state["Nashville"] = "TN"
# print(city_state)
# print(city_state["Seattle"])

print("--- List of cities and states enumerated")
for key,value in city_state.items():
    print(key,value)
print("--- END list of cities and states enumerated")


#Counters do a tally of uniques from a list of items
letters = ['B','B','A','B','C','A','B','B','A','C']
c = Counter(letters)
print(c)

# build list from departments to prepare for CSV import
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

# Multi-dimensional dictionaries
ceos = {
    "Elon Musk": {"company": "Tesla, SpaceX", "age": 49}, # He's actually 53
    "Tim Cook": {"company": "Apple", "age": 63},
    "Sundar Pichai": {"company": "Alphabet (Google)", "age": 51},
    "Satya Nadella": {"company": "Microsoft", "age": 56},
    "Mark Zuckerberg": {"company": "Meta (Facebook)", "age": 40},
    "Andy Jassy": {"company": "Amazon", "age": 56},
    "Jensen Huang": {"company": "NVIDIA", "age": 60},
    "Safra Catz": {"company": "Oracle", "age": 62},
    "Ginni Rometty": {"company": "IBM", "age": 66},
    "Lisa Su": {"company": "AMD", "age": 54},
    "Reed Hastings": {"company": "Netflix", "age": 63},
    "Daniel Ek": {"company": "Spotify", "age": 41},
    "Pat Gelsinger": {"company": "Intel", "age": 62},
    "Marissa Mayer": {"company": "Yahoo", "age": 49},
    "Dara Khosrowshahi": {"company": "Uber", "age": 54},
    "Shantanu Narayen": {"company": "Adobe", "age": 61},
    "Brian Chesky": {"company": "Airbnb", "age": 43},
    "Susan Wojcicki": {"company": "YouTube", "age": 55},
    "Ajay Banga": {"company": "Mastercard", "age": 64},
    "Daniel Zhang": {"company": "Alibaba", "age": 52}
}

print(ceos["Elon Musk"]["age"])
ceos["Elon Musk"]["age"] = 53
print(ceos["Elon Musk"]["age"])

for key,value in ceos.items():
    print(key)
    for key,value in value.items():
        print(key, value)