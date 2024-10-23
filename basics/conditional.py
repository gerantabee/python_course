# Conditional logic examples
'''
Syntax:

if condition:
    expression
elif condition:
    expression
else:
    expression
'''
grades = [55, 65, 75, 80, 91, 62, 50, 70]

# Try below with both 65 and 95
if 95 in grades:
    print("there is a 65")
elif 80 in grades:
    print("there is an 80")
else:
    print("Nothing found")

# Another example
state = "NY"
ordervalue = 25.00

# INDENTATION MATTERS!
# Let's calculate sales tax based on state and order value
if state == "NY":
  total = ordervalue + (ordervalue * .0825)
  print(total)
elif state == "MA":
  total = ordervalue + (ordervalue * .0625)
  print(total)
else:
  total = ordervalue
  print(total)


# If the order value is below a certain amount we can skip sales tax


# Another syntax
print(3 in [1, 2, 3] )

# Filtering using list comprehension
topgrades = [x for x in grades if x >= 80]
print(topgrades)

# Match / case
city = "Los Angeles"
match city:
    case "New York":
         print("NY")
    case "Los Angeles":
         print("CA")
    case "Dallas":
         print("Texas")
    case _:
        print("Unsure of state")


# Try and catch exceptions
# Defined tuple of days of week
days_of_week = ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday")

# Throws a TypeError
try:
    days_of_week[0] = "Funday"
except TypeError:
    print("TypeError occured")
