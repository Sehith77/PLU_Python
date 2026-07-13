# 7. Online Game Leaderboard
# An online gaming platform stores players' scores.
# Write a program to arrange the scores in descending order so that the
# leaderboard can be displayed.
scores = list(map(int, input("Enter player scores: ").split()))

for i in range(len(scores)):
    for j in range(len(scores) - 1 - i):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

print("Leaderboard:", scores)