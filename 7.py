# 7. Create student.txt, write your name, then read and display it.

file = open("Student.txt", "w")
file.write("snehith")
file.close()

file = open("Student.txt", "r")
data = file.read()
print(data)
file.close()

