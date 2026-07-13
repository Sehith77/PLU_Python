# # # arr = [10, 9, 100, 20, 5]

# # # n = len(arr)

# # # for i in range(n - 1):
# # # #     for j in range(n - 1 - i):
# # # #         if arr[j] > arr[j + 1]:
# # # #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # # # print(arr)



# # d = {"A": 1, "B": 5, "C": 2, "D": 4}

# # sorted_dict = dict(sorted(d.items(), key=lambda items : items[1]))
# # print(sorted_dict)

# A cricket coach has the scores of 15 players.

# # Requirements
# #     Accept scores of all players.
# #     Display the original list.
# #     Sort the scores using Bubble Sort.
# #     Display the sorted scores.
# #     Ask the coach to enter a player's score.
# #     Search for the score using Binary Search.
# #     Display the player's rank based on the sorted list.
# #     Also display:
# #         Highest score
# #         Lowest score
# #         Total number of players


# Algorithm

# Create an empty list to store player scores.
# Accept the scores of 15 players.
# Display the original list of scores.
# Sort the scores using the Bubble Sort algorithm.
# Display the sorted list.
# Ask the coach to enter a score to search.
# Perform Binary Search on the sorted list.
# If the score is found:
# Display "Score Found".
# Calculate the player's rank.
# If the score is not found:
# Display "Score Not Found".
# Display:
# Highest score
# Lowest score
# Total number of players
# Stop the program.
Scores = []

for in in range(15):
    s = int(input("Enter the score: "))
    scores.append(s)
    
print("Original:", Scores)

for i in range(14):
    for j in range(14 - i):
        if Scores[j] > Scores[j+1]:
            Scores[j], Scores[j + 1], Scores[j]

print("Sorted:", Scores)

x = int(input("Enter the search1: "))
low = 0
high = 14

while low <= high:
    mid = (low + high) // 2
    
    if Scores[mid]== x:
        print("")   
        