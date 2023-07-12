# Paul Claudel Izabayo, 06/29/2023
# Implemenation of a bag (assuming a bag that contains toys)

class Toy:
    def __init__(self):
        self.isInBag = False

class ToyBag:

    '''ToyBag accepts only Toy objects'''
    def __init__(self):
        self.size= 0

    def numToys(self):

        '''finds the number all toys in the bag'''
        return self.size

    def isEmpty(self):

        '''finds if the bag is empty'''
        if self.size == 0:
            return True
        else:
            return False
    
    def addToy (self, toy):

        '''adds a new toy to the bag'''
        toy.isInBag = True 
        self.size = self.size + 1
        return True
        
         
    def contains(self, toy):

        '''finds if a certain element is in the bag'''
        if self.size == 0:
            return False
        return toy.isInBag
    
    def remove (self, toy):

        '''removes an element from the bag'''
        if self.contains(toy):
            toy.isInBag = False
            self.size = self.size - 1 
            return toy

    def removeAll(self):
        '''removes all elements from the bag'''
        self.size = 0

################ End of the bag ################

'''A little demo'''
pig = Toy()
cam = Toy()
bag = ToyBag()
bag.addToy(cam)
bag.addToy (pig)
bag.removeAll ()
print (bag.numToys())
