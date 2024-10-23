# Lists
# "New York", "Chicago", "Boston"

# Let's put a watch for city == "" something
# for city in cities:
#     print(city)

# Add "Austin", "Orlando"
# print(cities2)

# Merging lists is as easy as the '+' operator
cities_all = cities + cities2

# Boolean type
# One of two fixed values, True or False (which are reserved terms)

# Use a for loop to test


# We can use enumerate to return both the index and value if needed
for index, city in enumerate(cities_all):
    print(index, city)

# List comprehension is a great shorthand to work through a list
# It can handle basic statements and conditions

# We can dissect lists or extradt specific elements by index or index range
# We can also use methods like append, pop, extend


# "NY","IL","MA","CA","TX","TX","OR", "OR"
states = ["NY","IL","MA","CA","TX","TX","OR", "OR"]

# Python set is mutable but items can't be changed, and it doesn't allow duplicates,
# It's a good way to reduce a list to unique values only


