def isBookExist(books, orderBookName):
    
    #check if orderbook name exists in the list of book objects
    
    for book in books:
        
        if book.bookName == orderBookName:
            print("found it!")
            return True

    return False

