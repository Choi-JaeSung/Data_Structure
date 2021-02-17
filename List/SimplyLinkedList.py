from Node import *

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
            return None
            
        else:
            node = self.head

            for i in range(0, index):
                node = node.getNext()
            
            return node
        
    def search(self, var):
        node = self.head
        
        for i in range(0, self.size):
            if node.getVar() == var:
                return node
            else:
                node = node.getNext()
                
        return None
    
    def deleteAt(self, index):
        if self.size == 0 or self.size <= index:
            return None
        else:
            if index == 0:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.getNext()
            else :
                current_node = self.head
                previous_node = self.head
                
                for i in range(0, index + 1):
                    if i == index:
                        if current_node.getNext() == None:
                            previous_node.setNext(None)
                            self.tail = previous_node
                        else:
                            previous_node.setNext(current_node.getNext())
                    else:    
                        previous_node = current_node
                        current_node = current_node.getNext()
            
            self.size -= 1
                        