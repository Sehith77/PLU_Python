# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     merged = []

#     while len(left) > 0 and len(right) > 0:
#         if left[0] < right[0]:
#             merged.append(left.pop(0))
#         else:
#             merged.append(right.pop(0))

#     merged = merged + left
#     merged = merged + right

#     return merged


# arr = [5, 2, 3, 8, 2, 3]

# print("Original Array:", arr)
# print("Sorted Array:", merge_sort(arr))

arr = [5, 2, 3, 8, 2, 3]

arr.sort()
print(arr)