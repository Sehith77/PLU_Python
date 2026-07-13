roll = list(map(int, input("Enter roll numbers: ").split()))

x = int(input("Enter roll number: "))

for i in range(len(roll)):
    if roll[i] == x:
        print("Student Found")
        print("Position:", i + 1)
        break
else:
    print("Student Not Found")
    
    

    