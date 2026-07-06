

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    
    def insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node


    def display(self, node, level=0):
        if node:
            print("   " * level + str(node.data))
            self.display(node.left, level + 1)
            self.display(node.right, level + 1)



tree = BST()


values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.root = tree.insert(tree.root, value)


tree.display(tree.root)
