# Paul Claudel Izabayo
# this is an Implemenation of the bag using a list 
# the size of the bag is predetermined

class ToyBag:
    def __init__(self):
        self.defaultSize = 25
        self.numEntries = 0
        self.bag = []

    def add (self,toy):
        '''adds an item to the bag'''
        if not self.isFull():
            self.bag.append(toy)
            self.numEntries = self.numEntries + 1
            return True
        else: 
            return False

    def remove (self,toy):
        '''removes an item from the bag'''
        if self.contains(toy):
           toyIndex = self.bag.index(toy)
           self.bag[toyIndex] = self.bag[self.numEntries - 1]
           self.bag[self.numEntries - 1] = None 
           self.numEntries = self.numEntries - 1

    def isFull(self):
        '''checks if the bag is full'''
        if self.numEntries == self.defaultSize:
            return True 
        else: 
            return False

    def contains(self,toy):
        '''checks if the bag contains a given item'''
        if self.numEntries == 0:
            return False
        for i in self.bag:
            if i == toy:
                return True
        return False

    def removeAll (self):
        '''removes all elements from the bag'''
        self.numEntries = 0
    
    def occurance (self,toy):
        '''counts how often an element occurs in the bag'''
        occ = 0
        for i in self.bag:
            if i == toy:
                occ = occ + 1
        return occ

    def toArray(self):
        '''turns the bag into an array'''
        bagArray = []
        for i in self.bag:
            bagArray.append(i)
        return bagArray

    def isEmpty(self):
        '''checks if the bag is empty'''
        if self.numEntries == 0:
            return True
        return False
    
    def remove(self):
        '''removes a random element from the bag.
        returns False if the element is not found.
        returns the element otherwise'''

        if self.isEmpty():
            return False
        else:
            toRemove = self.bag[self.numEntries-1]
            self.bag[self.numEntries-1] = None
            self.numEntries = self.numEntries - 1
            return toRemove

    def size(self): 
        '''returns the number of elements in the bag'''
        return self.numEntries

################## End of the bag #####################

'''A little demo'''

toybag = ToyBag()
toybag.add ("pupe")
toybag.add("mama")
toybag.add ("mtama")
toybag.add ("pupe")

print (toybag.remove())
print (toybag.contains("pupe"))
