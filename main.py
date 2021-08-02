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
    
    print(order.tag,order.book, order.operation, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))

    #check if book exists
    isBookFound = po.isBookExist(books,order.book )
    print(isBookFound)
    



