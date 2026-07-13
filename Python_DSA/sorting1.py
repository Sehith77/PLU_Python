

# a = [7, 3, 5, 9, 2, 12]

# for i in range(1, len(a)):
#     key = a[i]
#     j = i - 1
    
    
#     while j >= 0 and  a[j] >  key:
#         a[j + 1] =  a[j]
#         j = j - 1
        
#         a[j + 1] = key
#         print(a)
        
def quick(a):
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    left = []
    middle = []
    right = []

    for i in a:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)

    return quick(left) + middle + quick(right)

a = list(map(int, input("Enter elements: ").split()))

print("Original:", a)

a = quick(a)

print("Sorted:", a)