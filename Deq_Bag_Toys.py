# Paul Claudel Izabayo
# This is another implemenation of the bag using a deque (linked implemenation)

class ToyDeque:
    '''Main toy class'''

    class Node:
        '''Node definition'''

        def __init__(self,data):
            self.data = data
            self.next = None 

    def __init__(self):
        self.size = 0
        self.firstNode = None
    
    def  addToBack(self, toy):
        '''adds a toy at the back of the bag'''

        if self.isEmpty():
            self.firstNode = self.Node(toy)
            self.size = self.size + 1
        else:
            refNode = self.firstNode 
            while refNode.next != None:
                refNode = refNode.next
            refNode.next = self.Node(toy)
            self.size = self.size + 1

    def addToFront (self, toy):
        '''adds a toy at the front of the bag'''

        if self.isEmpty():
            self.firstNode = self.Node(toy)
            self.size = self.size + 1
        else:
            replaced = self.firstNode
            self.firstNode = self.Node (toy)
            self.firstNode.next = replaced
            self.size = self.size + 1 


    def removeFront (self):
        '''returns and removes a toy from the front of the bag'''

        
        if self.isEmpty():
            raise Exception ("The queue is empty! Please add toys first.")
        else:
            result = self.firstNode
            self.firstNode = self.firstNode.next
            self.size = self.size - 1
            return result.data

    
    def removeBack(self):
        '''returs and removes a toy from the back of the bag'''

        if self.isEmpty():
            raise Exception ("The bag is empty!")

        else:
            refNode = self.firstNode
            if refNode.next == None:
                result = refNode.data
                refNode = None 
                self.size = self.size - 1 
                return result
                
            while refNode.next.next != None:
                refNode = refNode.next
            result = refNode.next
            refNode.next = None
            self.size = self.size - 1
            return result.data
    
    def getFront (self):
        '''returns without removing the front element from the bag.'''

        if self.isEmpty():
            raise Exception ("The bag is empty. Please add toys.")
        else:
            return self.firstNode.data
    
    def getBack(self):
        '''returns without removing the back element from the bag.'''

        if self.isEmpty():
            raise Exception ("The bag is empty. Please add toys.")
        else:
            refNode = self.firstNode
            while refNode.next != None:
                refNode = refNode.next 
            return refNode.data

    def isEmpty(self):
        '''checks if the bag is empty.'''
        if self.size == 0:
            return True
        return False

    def clear (self):
        '''deletes all elements from the bag.'''
        self.size = 0

############# End of the bag ########################

'''A little demo'''


toybag = ToyDeque()

toybag.addToBack ("mama")
toybag.addToBack ("papa")
toybag.addToBack ("middle")
toybag.addToFront("dad")
toybag.addToFront("mum")

while not toybag.isEmpty():
    print (toybag.getFront())      
    