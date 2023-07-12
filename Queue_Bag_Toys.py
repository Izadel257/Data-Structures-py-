# Paul Claudel Izabayo
# This implementation of the bag uses a queue (linked implemenation)

class ToyQueue:
    '''The main bag class'''

    class Node:
        '''The node class definition '''

        def __init__ (self,data):
            self.data = data
            self.next = None

    def __init__ (self):
        self.firstNode = None
        self.size = 0

    def enqueue (self, toy):
        '''Adds an item at the back of the queue'''

        if self.isEmpty():
            self.firstNode = self.Node(toy)
            self.size = self.size + 1
        else:
            refNode = self.firstNode 
            while refNode.next != None:
                refNode = refNode.next
            refNode.next = self.Node(toy)
            self.size = self.size + 1

    def dequeue (self):
        '''Returns and remove the front element'''

        if self.isEmpty():
            raise Exception ("The queue is empty! Please add toys first.")
        else:
            result = self.firstNode
            self.firstNode = self.firstNode.next
            self.size = self.size - 1
            return result.data

    def isEmpty (self):
        ''''checks if the bag is empty'''

        if self.size == 0:
            return True
        return False
    
    def getFront (self):
        '''retrieves the front element without deleting it'''

        if self.isEmpty():
            raise Exception ("the queue is empty! Please add toys first.")
        else:
            return self.firstNode.data
    
    def clear(self):
        self.size = 0

############ End of the bag ################################################
'''A litle demo'''

toybag = ToyQueue()
toybag.enqueue ("papa")
toybag.enqueue ("mama")
toybag.enqueue ("dad")
toybag.enqueue ("wallah")
toybag.enqueue ("fam")


print (toybag.dequeue())
print (toybag.dequeue())
print (toybag.getFront())