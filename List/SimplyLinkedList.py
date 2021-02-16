from Node import Node

class SimplyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, var):
        node = Node(var)
        
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node
            
        self.size += 1
        
    def showList(self):
        print("SimplyLinkedList")
        node = self.head
        
        for i in range(0, self.size):
            print(node.getVar())
            node = node.getNext()
            
    def getAt(self, index):
        if self.size == 0 or self.size <= index:
            return print("Out of Range!")
            
        else:
            node = self.head

            for i in range(0, index):
                node = node.getNext()
            
            return node