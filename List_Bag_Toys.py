# Paul Claudel Izabayo
# This is an implementation of the bag that uses list (array implementation)
# The size of the bag is not limited. 

class ListToys:
    def __init__(self):
        self.bagArray = []
        self.size = 0

    def add (self,toy):
        '''Adds the element at the end of the list'''

        self.bagArray.append (toy)
        self.size = self.size + 1 
    
    def insert (self, position, toy):
        '''Adds the element at the given position (1 being the first position)'''

        if position < 1 or position > self.size:
            raise Exception ("Position out of range.")
        newArray = []
        for i in range (self.size):
            if i < position - 1:
                newArray.append (self.bagArray[i])
            elif i == position - 1:
                newArray.append (toy)
        missing = self.bagArray[position-1:self.size]
        if position == self.size:
            missing.append (toy)
        self.bagArray = newArray + missing
        self.size = self.size + 1

    def remove (self, position):
        '''Removes from the list the element at the given position.'''
        
        if position < 1 or position > self.size:
            raise Exception ("Position out of range.")

        newList = []
        deleted = self.bagArray[position-1]
        for i in range (0, self.size):
            if i < position - 1:
                newList.append (self.bagArray[i])
        remaining = self.bagArray[position:self.size]
        self.bagArray = newList + remaining
        self.size = self.size - 1 
        return deleted 

    def replace(self,position, toy):
        '''Replaces the element at the given position with the new element'''

        if position < 1 or position > self.size:
            raise Exception ("Position out of range")
        replaced = self.bagArray[position-1]
        self.bagArray[position-1] = toy
        return replaced 

    def getEntry(self, position):
        '''retrieves the entry at the given position.'''
        if position < 1 or position > self.size:
            raise Exception ("Position out of range")
        return self.bagArray[position-1]

    def toArray (self):
        '''returns an array containing all the elements of the bag'''

        return self.bagArray
    
    def contains (self, toy):
        '''checks if the bag contains the given element'''

        if toy in self.bagArray:
            return True 
        return False
    
    def getLength (self):
        '''finds the total number of elements in the bag.'''

        return self.size 

    def isEmpty(self):
        '''checks if the  bag is empty'''

        if self.size == 0:
            return True 
        return False 
    def clear (self):
        '''deletes all elements from the bag.'''
        self.bagArray.clear()
        self.size = 0

#########End of the bag##########################

'''A little Demo'''
toybag = ListToys()

toybag.add ("mama")
toybag.add ("papa")
toybag.add ("manuel")
toybag.add ("eleeh")
toybag.add ("nanje")

toybag.insert (1,"Keys")
toybag.insert (3,"mama")
toybag.insert (4,"prince")
toybag.insert (8,"success motherfucker")
toybag.insert (9, "wallah vyakunze")
toybag.remove (9)
toybag.remove (1)
toybag.remove (2)


print (toybag.getLength())
toybag.clear()
print (toybag.getEntry (3))
print (toybag.toArray())
