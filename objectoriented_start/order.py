class Order(object):
    _total: float
    _taxrate = .0825

    def __init__(self, item, qty, price):
        self._item = item
        self._qty = qty
        self._price = price
        self._total = qty * price

    def __str__(self):
        return self._item

    def calctaxes(self):
        self._total + (self._total * self._taxrate)
        return self

    def addHandling(self):
        self._total += 7.50
        return self

    def addShipping(self):
        self._total += self._total * .15
        return self

    @property
    def total(self):
        return round(self._total,2)


def buildOrder(item, qty, price):
    order = Order(item, qty, price)
    finalprice = order.calctaxes().addHandling().addShipping()
    print(finalprice.total)



if __name__ == '__main__':
    buildOrder("Bike", 1, 150.00)
