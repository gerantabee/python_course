# Debug, step into, run to cursor, etc.
orders = []
orders.append(["Bike",119.99])
orders.append(["Sneakers",59.99])
orders.append(["Album",29.99])

def calctaxes(price):
    # Run to cursor
    return price * .0825
    # return price + (price * .0825)

def addhandling(price):
    return price * .10
    # return price + (price * .10)

def addshipping(price):
    return price + 7.50

def calculateTotals(orders):
    i = 0
    for order in orders:
        price = calctaxes(order[1])
        price = addhandling(price)
        price = addshipping(price)
        # print(round(price,2))
        orders[i][1] = round(price,2)
        i += 1

calculateTotals(orders)

# List comprehension
[print(x[1]) for x in orders]
