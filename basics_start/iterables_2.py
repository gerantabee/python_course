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
# use ["element"], update, keys() and values()

# We can loop through dictionaries in a similar way to lists

# Use items() and variable pairs (i,j) to access keys and values in a loop



states = ["NY","IL","MA","CA","TX","TX","OR"]
cities = ["New York","Chicago","Boston", "Los Angeles", "Dallas", "Austin", "Portland"]

# Let's create a dictionary called city_state to unite the states and cities


# Unite the lists using enumerate




print("--- List of cities and states enumerated")

print("--- END list of cities and states enumerated")


# Counters returns a dict tally of uniques from a list of items
# from collections import Counter to use it
letters = ['B','B','A','B','C','A','B','B','A','C']


# Reading CSVs into iterables for manipulation
departments = []



# Use Counter to create a tally of departments!


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

