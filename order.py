import time

class Order:
    def __init__(self,tag, book, operation, price, volume, orderID):
        self.tag = tag
        self.book = book
        self.operation = operation
        self.price = float(price)
        self.volume = float(volume)
        self.orderID = orderID
        self.timeStamp = time.time()
        

