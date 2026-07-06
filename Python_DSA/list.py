n = self.head

while n is not None:
    print(n.data)
    n = n.ref
    