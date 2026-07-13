# 8. Hospital Emergency Queue
# A hospital has a list of patients with different priority levels.
# Write a program to arrange the patients so that the patient with the
# highest priority is treated first
patients = list(map(int, input("Enter patient priorities: ").split()))

for i in range(len(patients)):
    for j in range(len(patients) - 1 - i):
        if patients[j] < patients[j + 1]:
            patients[j], patients[j + 1] = patients[j + 1], patients[j]

print("Emergency Queue:", patients)