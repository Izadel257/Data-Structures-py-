# Paul Claudel Izabayo
# This is an emplementation of the bag as a linked-list-stack

class ToyStack:
    ''' The toy class'''
    class Node:
        '''A node class to contain for the linked list'''
        def __init__ (self,data):
            self.data = data
            self.next = None

    def __init__ (self):
        self.size = 0
        self.firstNode = None
    
    def push (self, toy):
        '''Adds an item at the top of the list'''
        if self.isEmpty():
            self.firstNode = self.Node(toy)
            self.size = self.size + 1
        else:
            refNode = self.firstNode 
            while refNode.next != None:
                refNode = refNode.next
            refNode.next = self.Node(toy)
            self.size = self.size + 1

    def pop(self):
        '''return and removes the top element of the list'''
        if self.isEmpty():
            raise Exception ("The bag is empty!")

        else:
            refNode = self.firstNode
            if refNode.next == None:
                result = refNode
                refNode = None 
                self.size = self.size - 1 
                return result.data
                
            while refNode.next.next!= None:
                refNode = refNode.next
            result = refNode.next
            refNode.next = None
            self.size = self.size - 1
            return result.data

    def peek(self):
        '''returns without removing the top element of the list'''
        if self.isEmpty():
            raise Exception ("Bag is empty!")
        else:
            refNode = self.firstNode
            while refNode.next != None:
                refNode = refNode.next
            result = refNode
        return result.data

    def isEmpty(self):
        '''checks if the bag is empty'''
        if self.size == 0:
            return True 
        else:
            return False
    def clear(self):
        '''deletes all the elements from the stack'''
        self.size = 0

############# End of the stack##########################

'''A little demo'''
toybag = ToyStack()
toybag.push ("paul")
toybag.push ("pul")
toybag.push ("pal")
toybag.push ("pau")
toybag.push ("paula")
toybag.push ("aul")
while not toybag.isEmpty():
    print (toybag.pop())
toybag.push ("lau")
#toybag.clear() 
print (toybag.size)
print (toybag.peek())
