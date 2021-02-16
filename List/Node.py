class Node:
    def __init__(self, var):
        self.var = var
        self.next = None
        
    def getVar(self):
        return self.var
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next