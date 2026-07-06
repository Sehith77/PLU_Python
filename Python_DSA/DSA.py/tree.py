class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeStructure:
    def createRoot(self, data):
        self.root = Node(data)
        
    def insertNode(self, data):
        self.new_node =Node(data)
        if self.root.left == None:
            self.root.left = self.new_node
        elif self.root.right == None:
            self.root.right = self.new_node
            
        else :
            print("move to the next level as the root is connected to two nodes ")
    def left(self, root_node, node):
        root_node.left = node
    
    def left(self, root_node, node):
        root_node.left = node
        
    def move_to_next(self, node):
        next_node = 0
        if node.left:
            return next_node = node.left
        else:
            return next_node = node.right
        
        
class BinaryTree:
    def deleteNode(Self, data):
        self.root = self.delete_rec(self.root, data)
        
        def _delte_rec(self, node, data):
            if node is None:
                return node
            
        if data < node.data:
            node.left 
            
            
    

        