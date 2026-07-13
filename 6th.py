# 6. Employee Salary Report
# An HR department has employee salary records collected from two different
# branches.
# Write a program to combine both lists and display all salaries in
# ascending order.
salary1 = list(map(int, input("Enter Branch 1 salaries: ").split()))
salary2 = list(map(int, input("Enter Branch 2 salaries: ").split()))

salary = salary1 + salary2
for i in range(len(salary)):
    for j in range(len(salary) - 1 - i):
        if salary[j] > salary[j + 1]:
            salary[j], salary[j + 1] = salary[j + 1], salary[j]

print("Sorted Salaries:", salary)
