import readXML as xmlReader
from datetime import datetime
import book as orderBook
import processOrder as po


#read all attributes in the xml file and return root
xmlOrders = xmlReader.ParseXMLFile('test.xml')
    
#create array of book objects
books = [orderBook.Book('book-1'),orderBook.Book('book-5')]

orders = []

for xmlOrder in xmlOrders:
    
    #convert xml order to an object    
    order = xmlReader.getOrderObject(xmlOrder)
    
    #print(order.tag,order.book, order.operation, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))
    
    #get the book name if it exists, else return nothing
    book = po.isBookExist(books,order.book)
    
    
    if  book == None:
        
        #create new orderbook
        book = orderBook.Book(order.book)
        
        #add new book to the list of books
        books.append(book)
        
    #add order to book
    po.addOrderToBook(book, order)  
        

#test if the books were populated with the orders

for book in books:
    
    print(book.bookName)
    for order in book.sellOrders:
              
        print(order.tag,order.book, order.operation, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))   
        
    



