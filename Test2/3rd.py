# 3.Delete the node containing 30 from the linked list and display the updated list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

n2.next = n4

temp = n1

while temp is not None:
    print(temp.data)
    temp = temp.next
        

    