# Functions are resuable code structures, that allow us to encapsulate a set of statements
# that can be re-used
# Functions can return a value, perform a task (or both) and can be fed pieces of information
# known as arguments (or parameters).

#Syntax uses 'def' to create a function
def myFunction():
    print("My first function")

# Let's create returnMessage, and printMessage with a param


#########
# Function to calculate taxes


# you can also use Error handling to manage invalid data types
# Python doesn't enforce param data types, so we may have to add error handlling
def calcTaxes(cost:float,taxrate:float):
    total = (cost * taxrate) + cost
    print(total)


calcTaxes(25,.08625)

# Functions can take arbitrary numbers of arguments as well using *args
# A function that can take varying arguments of the same theme would be impractical to map out

# Use the list below:
# "AAPL","MSFT","GOOGL","AMZN", "KO"
def stocks():
  pass



# You can also use the **kwargs, which maps argument values to keywords, regardless of order
# Let's define a function called carprofile that takes arbitrary key:value pairs


def carprofile(**kwargs):
  pass

# carprofile(make="Toyota", model="Camry", year="2024")

# We can combine different types of args
def carprofile2():
  pass

# options = ["ac","backup camera", "4WD","moonroof","premium sound"]
# carprofile2(35000,"backup camera", "heated seats", make="Toyota", model="Camry", year="2024")

'''
Lambda functions
Automatically return (do not require a return statement)
Along with map and filter
'''

'''
Syntax:
lambda argument: argument + expression
'''




# Filter an iterable using lambda functions
grades = [55, 65, 75, 80, 91, 62, 50, 70]

# Filters always return filter objects which need to be converted to lists


# Maps apply a function to each element in an iterable
# As with filter, maps return map objects which need to be converted to lists
