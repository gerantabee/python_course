from models.orders import OrderItem
from models.orders import Order


def main():
    # Avoid stepping into scripts or libraries
    item1 = OrderItem("Bike", 299.99, 1)
    item2 = OrderItem("Basketball", 19.99, 2)
    item3 = OrderItem("Tennis Racket", 140.99, 1)
    #item4 = "Football"
    order = Order()
    order.appendItem(item1)
    order.appendItem(item2)
    order.appendItem(item3)
    #order.appendItem(item4)
    # # Debug why we are getting Order Item instead of the item name
    # # Evaluate variables and step into
    order.getall()

main()




