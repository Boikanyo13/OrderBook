import readXML as xmlReader

#read all attributes in the xml file
    
orders = xmlReader.ParseXMLFile('test.xml')

#test if orders are stored in the array
for order in orders:
    print(order.tag,order.book, order.operation)

