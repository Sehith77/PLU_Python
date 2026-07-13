# 3. Arrange Exam Marks
# A teacher wants to display students' marks from the lowest to the
# highest.
# Write a program to sort the marks of all students in ascending order.
marks = list(map(int, input("Enter marks: ").split()))
for i in range(len(marks)):
    for j in range(len(marks)-1 -i):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j+1] = marks[ j + 1], marks[j]
            
            print("Sorted Marks:", marks)