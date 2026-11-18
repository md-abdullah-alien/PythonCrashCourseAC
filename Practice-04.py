# Question-01:
# Print all odd numbers from 1 to 20
# Brute Force Approach
for i in range(1, 20):
    if(i%2 == 0):
        print(i)

# Efficient Approach
for i in range(2, 20, 2):
    print(i)


# Question-02: Print the table of 57
# Brute Force Approach
for i in range(57, 571):
    if(i%57 == 0):
        print(i)

# Efficient Approach
for i in range(57, 571, 57):
    print(i)


# Question-03: Print all multiples of 3 from 1 to 50 but skip 15
for i in range(1, 50):
    if(i == 15):
        continue
    if(i%3 == 0):
        print(i)


# Question-04: Take two integers a and b as input.
# Find and print the first number between 1 and 1000 that divisible by both numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for i in range(1, 1000):
    if(i%a == 0 and i%b == 0):
        print(i)
        break

