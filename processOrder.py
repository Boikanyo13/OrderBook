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
            
            book = book.sellOrders.remove(order)
                  
    return book