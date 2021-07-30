#* import libaries

import xml.etree.ElementTree as ET


# parse the xml file
tree = ET.parse('test.xml')
orders = tree.getroot()

# print(orders)
# print(orders[0].attrib)
# print(orders[0].tag)


#read all attributes in the xml file

for order in orders:
    print(order.tag, order.attrib)