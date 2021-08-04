import readXML as xmlReader
from datetime import datetime
import book as orderBook
import processOrder as po
import itertools as it
import os
import time


# read all attributes in the xml file and return root
xmlOrders = xmlReader.ParseXMLFile('data/orders.xml')
    
# create array of book objects
books = []

for xmlOrder in xmlOrders:
    
    # convert xml order to an object    
    order = xmlReader.getOrderObject(xmlOrder)
    
    
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
    
           
    #display the changes in the orderbooks
    for book in books:
        
        print('\n================', book.bookName, '================\n')
        print('\n ====BUY====\t    ====SELL====\n')
        
        for sellOrder, buyOrder in it.zip_longest(book.sellOrders,book.buyOrders):
            
            
            if(buyOrder != None):
                print(buyOrder.orderID, buyOrder.price, '@',buyOrder.volume,end='')
            
            else:
                print('\t',end='')
            
            if(sellOrder != None): 
                print('\t--',sellOrder.orderID, sellOrder.price, '@',sellOrder.volume )
            else:
                print('')
            
            
        print('\n=================================================\n')
    
    time.sleep(0.25)
    os.system('clear')
     



