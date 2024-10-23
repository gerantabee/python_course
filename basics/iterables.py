# Lists
# "New York", "Chicago", "Boston"
cities = []
cities = ["New York", "Chicago", "Boston"]
cities.append("Los Angeles")

# Let's put a watch for city == "" something
# for city in cities:
#     print(city)

cities2 = ["Austin", "Orlando"]
# print(cities2)

# Merging lists is as easy as the '+' operator
cities_all = cities + cities2
cities3 = ["Dallas","Portland"]

# Boolean type
containsNY = False
print(cities_all)

for city in cities_all:
    # Use casefold() for non-case comparison
    city = city.casefold()
    if city == ("New York").casefold():
        containsNY = True
        print(containsNY)

for index, city in enumerate(cities_all):
    print(index, city)

# List comprehension
[print(city.upper()) for city in cities]

print(cities_all[:3])
cities_all.pop()
print(cities_all) # Removes Orlando
cities_all.extend(cities3)
print(cities_all)

# "NY","IL","MA","CA","TX","TX","OR"
states = ["NY","IL","MA","CA","TX","TX","OR"]

# Python set is mutable but items can't be changed, and it doesn't allow duplicates,
states_set = set(states)
# This will only print uniques
[print(x) for x in states_set]
print(len(states_set))


