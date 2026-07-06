from collections import deque

stack_container = deque()

var = input("Enter the value: ")

stack_container.append(var)

print("Stack:", stack_container)

print("Stack after pop:", stack_container)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        if len(self.queue) == 0:
            return "Queue is Empty"
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
   