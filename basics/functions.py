# Functions are resuable code structures, that allow us to encapsulate a set of statements
# that can be re-used
# Functions can return a value, perform a task (or both) and can be fed pieces of information
# known as arguments (or parameters).

#Syntax uses 'def' to create a function
def myFunction():
    print("My first function")

def returnMessage():
    return "My first function"

def printMessage(message:str):
    print(message)

myFunction()
print(returnMessage())
printMessage("Hey everyone")

#########
# Function to calculate taxes
def calcTaxes(cost:float,taxrate:float):
  total = (cost * taxrate) + cost
  # print(total)
  return total


ct = calcTaxes(25, .0825)
print("Total taxes and cost:",ct)

# you can also use Error handling to manage invalid data types
def calcTaxes(cost:float,taxrate:float):
  try:
    total = (cost * taxrate) + cost
    print(total)
  except TypeError:
    print("Invalid data type")
  except ValueError:
    print("syntax issue")

calcTaxes(25,.08625)

# Functions can take arbitrary numbers of arguments as well using *args
# A function that can take varying arguments of the same theme would be impractical to map out
def stocks(*args):
  for arg in args:
    print(arg)

# Use the list below:
# "AAPL","MSFT","GOOGL","AMZN"

stocks("AAPL","MSFT","GOOGL","AMZN","KO")

# You can also use the **kwargs, which maps argument values to keywords, regardless of order
def carprofile(**kwargs):
  profile = dict(**kwargs)
  print(profile['make'])
  for i in profile:
    print(i, ":", profile[i])

carprofile(make="Toyota", model="Camry", year="2024")

def carprofile2(price:int, *args, **kwargs):
  print("Price:",price)
  profile=dict(kwargs)
  for i in profile:
    print(i.upper(), ":", profile[i])
  for i in args:
    print(i)

# options = ["ac","backup camera", "4WD","moonroof","premium sound"]
carprofile2(35000,"backup camera", "heated seats", make="Toyota", model="Camry", year="2024")

'''
Lambda functions
Automatically return (do not require a return statement)
Along with map and filter
'''

'''
Syntax:
lambda argument: argument + expression
'''

tax=lambda n:n + (n * .0825)
print(tax(7.00))

(lambda n:n + (n * .0825))(19.99)

grades = [55, 65, 75, 80, 91, 62, 50, 70]
grades2 = filter(lambda n:n >= 80, grades)
# Filters always return filter objects which need to be converted to lists
print(list(grades2))

# As with filter, maps return map objects which need to be converted to lists
grades3 = map(lambda n:n + 10, grades)
print(list(grades3))
