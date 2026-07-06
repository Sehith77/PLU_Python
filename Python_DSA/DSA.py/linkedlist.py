class Node:
    def __init__( self, data ):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
    self.head=None
    
    def insert_start(self, data):
    new_node= Node(data)
    new_node.ref = self.head
    self.head = new_node
    
def insert_betw(self, data, prev):
    new_node = Node(data)
    new_node.ref = prev.ref
    prev.ref = new_node
    
def insert_end(self, data):
    new_node = Node(data)

    #   This line checks whether the linked list is empty
    if self.head is None:
         
        self.head = new_node
        # Starts traversal from the first node.
    else:
        n = self.head
        # Keep moving until the last node.
        while n.ref is not None:
            # It moves n to the next node until the last node is reached.
            n = n.ref
            # This connects the last node to the new node
        n.ref = new_node
        
        n = self.head

def search(self, data):
        n = self.head

        while n is not None:
            if n.data == data:
                print("Node Found")
                return
            n = n.ref

        print("Node Not Found")

def del_start(self):
        del_node = self.head
        self.head = self.head.ref
        del_node.ref = None
        
def del_bet(self, prev):
    prev.ref = prev .ref.ref
    prev.ref.ref = None
    
def del_end(self):
    n = self.head

    while n.ref.ref is not None:
        n = n.ref

    del_node = n.ref
    n.ref = None
    del_node.ref = None


def delete_end(self):
    if self.head is None:
        print("Linked List is Empty")
        
    elif self.head.ref is None:
        self.head = None
        
    else:
        n=self.head
        while n.ref is not None:
            
        n = n.ref = None
        
        
        
        