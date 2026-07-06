# 2.Insert a new node containing 25 after the node containing 20
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

new = Node(25)
new.next = n2.next
n2.next = new
temp = n1
while temp is not None:
    print(temp.data)
    temp = temp.next
    
    