import xml.etree.ElementTree as ET
import order as od

def ParseXMLFile(filename):
    #read orders in xml file and return orders array
    
    tree = ET.parse(filename)  
    rawOrders = tree.getroot()
    
    orders = []
    
    
    for rawOrder in rawOrders:
        
        #create the order object      
        order = od.Order(rawOrder.tag, rawOrder.get(key='book'), rawOrder.get(key='operation'), rawOrder.get(key='price'), rawOrder.get(key='volume'), rawOrder.get(key='orderID'))
        
        orders.append(order)
        
    return orders
