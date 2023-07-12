 # Paul Claudel Izabayo
 # An implemenation of the bag as a linked list

class ToyBag:
    def __init__(self):
        self.size = 0
        self.firstNode = None

    def add(self,toy):
        '''Add a new toy to the bag'''
        if self.isEmpty():
            self.firstNode = Node(toy)
            self.size = self.size + 1
        else:
            refNode = self.firstNode 
            while refNode.next != None:
                refNode = refNode.next
            refNode.next = Node(toy)
            self.size = self.size + 1
    def remove (self, toy):
        '''removes a specific toy from the bag'''
        if toy == self.firstNode.data:
            firstNode = self.firstNode.next
            self.size = self.size - 1
        else:
            if self.contains(toy):
                refNode = self.firstNode
                while refNode.next.data != toy:
                    refNode = refNode.next
                toDel = refNode.next
                if refNode.next.next != None:
                    refNode.next = refNode.next.next
                    toDel.next = None
                else:
                    refNode.next = None
                self.size = self.size - 1  

    def contains (self,toy):
        '''checks if the bag contains a given item'''
        if self.isEmpty():
            return False
        elif toy == self.firstNode.data:
            return True
        refNode = self.firstNode
        while refNode.next != None:
            refNode = refNode.next 
            if refNode.data == toy:
                return True
        return False 
    
    def isEmpty(self):
        '''checks if the list is empty or not'''
        if self.size == 0:
            return True
        return False
    
    def removeAll (self):
        '''removes all elements from the list'''
        self.size = 0
        self.firstNode = None 
    
    def occurance (self,toy):
        '''checks out how often a given element appears in the bag'''
        occ = 0
        refNode = self.firstNode
        while refNode!= None:
            if refNode.data == toy:
                occ = occ + 1
            refNode = refNode.next     
        return occ

    def toString(self):
        if self.isEmpty():
            return 
        else:
            refNode = self.firstNode
            theString = self.firstNode.data.data
            while refNode.next != None:
                refNode = refNode.next
                theString = theString + "|-->" +refNode.data.getData()
        print (theString)


class Node:
    '''Node class definition'''
    def __init__(self, data):
        self.data = data
        self.next = None 
    def getData(self):
        return self.data
################# End of the bag ###################

'''a little demo'''

toybag = ToyBag()
papa = Node("papa")
mama = Node ("mama")
maa = Node ("mama")
pups = Node ("pups")
mum = Node ("mum")

toybag.add (papa)
toybag.add (mama)
toybag.add (maa)
toybag.add (mama)
toybag.add (pups)
toybag.removeAll()
toybag.toString()