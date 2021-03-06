import xml.etree.ElementTree as ET
import order as od
import deleteOrder as deleteOd

def ParseXMLFile(filename):
    #read orders in xml file and return orders array
    
    tree = ET.parse(filename)  
    xmlOrders = tree.getroot()
    
    return xmlOrders

def getOrderObject(xmlOrder):   
    #create and return the order object      
    
    if xmlOrder.tag == 'AddOrder':
        order = od.Order(xmlOrder.tag, xmlOrder.get(key='book'), xmlOrder.get(key='operation'), xmlOrder.get(key='price'), xmlOrder.get(key='volume'), xmlOrder.get(key='orderId'))
    
    elif xmlOrder.tag == 'DeleteOrder':
        order = deleteOd.DeleteOrder(xmlOrder.tag, xmlOrder.get(key='book'), xmlOrder.get(key='orderId'))
        
    return order
