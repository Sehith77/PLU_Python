# 10. School Annual Report
# A school has recorded the marks of 50 students.
# Write a program that:
# Sorts the marks in ascending order.
# Accepts a mark from the user.
# Checks whether that mark exists in the sorted list.
# Displays the position if found; otherwise, prints "Mark Not Found."
marks = list(map(int, input("Enter marks: ").split()))

for i in range(len(marks)):
    for j in range(len(marks)-1-i):
        if marks[j] > marks[j+1]:
            marks[j], marks[j+1] = marks[j+1], marks[j]

print("Sorted:", marks)

x = int(input("Enter mark: "))

low = 0
high = len(marks)-1

while low <= high:
    mid = (low+high)//2

    if marks[mid] == x:
        print("Found at Position", mid+1)
        break
    elif x < marks[mid]:
        high = mid-1
    else:
        low = mid+1
else:
    print("Mark Not Found")