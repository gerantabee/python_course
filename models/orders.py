class OrderItem():
    _item: str
    _price: float
    _quantity: int

    def __init__(self, item, price, quantity):
        self._item = item
        self._price = price
        self._quantity = quantity
        print("New order created: {}, {}: {}".format(self._item, self._price, self._quantity))


    def __str__(self):
        print("Order instance for {}".format(self.item))
        # We should define a return name for this order
        return "Order Item"
        # return self._item

    @property
    def item(self):
        return self._item

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, qty):
        self._quantity = qty


class Order():
    def __init__(self):
        self._items = []

    def appendItem(self, orderitem):
        self._items.append(orderitem)

    def getall(self):
        for item in self._items:
            # Use Evaluate Expression
            # print("Order item: {} price: {} qty: {}".format(str(item), item.price, item.quantity))
            print("Order item: {} price: {} qty: {}".format(str(item), item.price, item.quantity))




item1 = OrderItem("Bike", 299.99, 1)
item2 = OrderItem("Basketball", 19.99, 2)
item3 = OrderItem("Tennis Racket", 140.99, 1)

if __name__ == '__main__':
    ordr = Order()
    ordr.appendItem(item1)
    ordr.appendItem(item2)
    ordr.appendItem(item3)
    # Debug why we are getting Order Item instead of the item name
    # Evaluate variables and step into
    ordr.getall()

