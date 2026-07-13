# 9. Library Book Search
# A library has 10,000 books, and the Book IDs are already arranged in
# ascending order.
# Write a program to find a given Book ID efficiently.
# Also mention which searching algorithm you used and why it is suitable.
books = list(map(int, input("Enter Book IDs: ").split()))

x = int(input("Enter Book ID to search: "))

low = 0
high = len(books) - 1

while low <= high:
    mid = (low + high) // 2

    if books[mid] == x:
        print("Book Found")
        print("Index:", mid)
        break
    elif x < books[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Book Not Found")