import readXML as xmlReader
from datetime import datetime


#read all attributes in the xml file and return root
xmlOrders = xmlReader.ParseXMLFile('test.xml')
    
#create array of books
books = []

orders = []

for xmlOrder in xmlOrders:
    
    #convert xml order to an object    
    order = xmlReader.getOrderObject(xmlOrder)
    
    print(order.tag,order.book, order.operation, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))
        
    orders.append(order)



