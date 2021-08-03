import readXML as xmlReader
from datetime import datetime
import book as orderBook
import processOrder as po


# read all attributes in the xml file and return root
xmlOrders = xmlReader.ParseXMLFile('test.xml')
    
# create array of book objects
books = []

for xmlOrder in xmlOrders:
    
    # convert xml order to an object    
    order = xmlReader.getOrderObject(xmlOrder)
    
   
    #print(order.tag,order.book, order.operation, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))
    
    # get the book name if it exists, else return nothing
    book = po.isBookExist(books,order.book)
      
    if  book == None:
        
        # create new orderbook
        book = orderBook.Book(order.book)
        
        # add new book to the list of books
        books.append(book)
        
        # add order to book
        if order.tag == 'AddOrder': 
            po.addOrderToBook(book, order) 
    
    else:
        
        if order.tag == 'AddOrder': 
            
            # process the order        
            po.AddOrderProcess(book, order)
        
        # Delete order
    
        elif order.tag == 'DeleteOrder':
        
            book =  po.DeleteOrder(book, order)
       
     

# test if the books were populated with the orders

for book in books:
    
    print('\n========', book.bookName, '========\n')
    for order in book.sellOrders:
              
        print(order.orderID, order.price, order.volume)# datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))   
        
    # for order in book.buyOrders:
              
    #     print(order.tag,order.book, order.operation,order.orderID, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))   
    print('\n===========================\n')
        
    



