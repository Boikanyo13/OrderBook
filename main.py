import readXML as xmlReader
from datetime import datetime

#read all attributes in the xml file
    
orders = xmlReader.ParseXMLFile('test.xml')

#test if orders are stored in the array
for order in orders:
    print(order.tag,order.book, order.operation, datetime.utcfromtimestamp(order.timeStamp).strftime('%Y-%m-%d %H:%M:%S.%f'))

