# 4. Rank Participants
# A sports academy has recorded the timings (in seconds) of participants in
# a race.
# Write a program to arrange the timings from the fastest to the slowest so
# that the winners can be announced



time = list(map(int, input("Enter timings: ").split()))
for i in range(len(time)):
    for j in range(len(time) - 1 - i):
        if time[j] > time[j + 1]:
            time[j], time[j+1] = time[j +1 ], time[j]
            print("Ranked Timings:", time)
            