# Question-01:
# Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110].
# Print all unique roll numbers in the list.

numbers = {101, 105, 102, 101, 108, 105, 110}
print(numbers)


# Question-02:
# Given Employee records in the form of a list of tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)
# Example: [
#           (101, "Alice", 50000),
#           (102, "Bob", 65000),
#           (103, "Charlie", 45000)
#           ]


Employees = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

ID = int(input("Enter Employee ID to search: "))
found = False

for E in Employees:
    if E[0] == ID:
        print("Employee Found!")
        print("Employee ID:", E[0])
        print("Employee Name:", E[1])
        print("Salary:", E[2])
        found = True
        break
if not found:
    print("Employee not found!")


