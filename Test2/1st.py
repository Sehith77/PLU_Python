# 1.Create a linked list containing the values 10, 20, 30, 40, 50 and display all the elements.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

temp = n1
while temp is not None:
    print(temp.data)
    temp = temp.next
    