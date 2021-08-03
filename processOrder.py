import order as od

def isBookExist(books, orderBookName):
    
    #check if orderbook name exists in the list of book objects
    
    for book in books:
        
        if book.bookName == orderBookName:
            
            return book

    return None


def addOrderToBook(book, order):
    
    #append the order to the book depending on the operation
    
    if order.operation == 'SELL':
        
        book.sellOrders.append(order)
        
    elif order.operation == 'BUY':
        
        book.buyOrders.append(order)
    
    return book

def DeleteOrder(book, incommingOrder):
    # delete order from the book
    
    for order in book.buyOrders:
        
        if order.orderID == incommingOrder.orderID:
            
            book = book.buyOrders.remove(order)
            
            #in case sure if we will ever delete from sell order
            #book = book.sellOrders.remove(order)
                  
    return book

def AddOrderProcess(book, incomingOrder):
    
    if incomingOrder.operation == 'BUY':
        
        addOrderBuy(book, incomingOrder)
    
    
        
def addOrderBuy(book, incomingOrder):
    
    #process orders with addOrder message
    
    if len(book.sellOrders) > 0:
        
      minprice = min(book.sellOrders, key=lambda x: x.price).price

      if incomingOrder.price >= minprice:

          minArray = list(filter(lambda x: x.price == minprice, book.sellOrders))

          #if there are more qualifying orders
          if(len(minArray)) > 1:

              earliestOrder = min(minArray, key=lambda x: x.timeStamp)
         
              if incomingOrder.volume <= earliestOrder.volume:
                  earliestOrder.volume = earliestOrder.volume - incomingOrder.volume

              else:
                  incomingOrder.volume = incomingOrder.volume - earliestOrder.volume
                  book.sellOrders = list(filter(lambda x: x.orderID != earliestOrder.orderID, book.sellOrders))
                  addOrderBuy(book, incomingOrder)

          else:

              earliestOrder = minArray[0]

              if incomingOrder.volume <= earliestOrder.volume:
                earliestOrder.volume = earliestOrder.volume - incomingOrder.volume

              else:
                incomingOrder.volume = incomingOrder.volume - earliestOrder.volume
                book.sellOrders = list(filter(lambda x: x.orderID != earliestOrder.orderID, book.sellOrders))
                addOrderBuy(book, incomingOrder)

      else: 
        book.buyOrders.append(incomingOrder)
        
    else: 
        book.buyOrders.append(incomingOrder)
      