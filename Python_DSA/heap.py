arr = [5, 7, 2, 4, 8]
n = len(arr)

for i in range(n):
    print("Parent:", arr[i])
    
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n:
        print("Left Child :", arr[left])
        
        if right < n :
            print("Right Child:", arr[right])
            
            print()
            