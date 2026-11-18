# Topics of Chapter Four
# 01. Range
# 02. while Loop
# 03. for Loop
# 04. break & continue
print("Welcome to Chapter Four")

# About Range
# range(start, stop, step)
# start ==> Where to start. By default value = 0
# stop ==> Where to stop. Must input it.
# step ==> Value of increase or decrease.  By default value = 1

range(5) # [0, 1, 2, 3, 4]
# range(n) # Output: [0 to n-1]
print(range(5)) # Output: range(0, 5==n-1) means range(0, 5<n)

# range 1 to 5
print(range(0, 6))

# range 2 to 100 even number
print(range(2, 100, 2))

# Work with while loop
# Loops means repeated one thing again & again
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")

# while condition:
#     print("Hello World!")

a = 1
while a <=50:
    print(a,"Hello World!")
    a += 1
print("Ended the increasing code!!!")

b = 50
while b >=0:
    print(b,"Hello World!")
    b -= 1
print("Ended the decreasing code!!!")

# Infinite Loop
# c = 50
# while c >=0:
#     print(c,"Hello World!")
# Without increment or decrement operations

d = 1
while d <= 10:
    print(d * "*") # Done by string concatenation
    d += 1

e = 10
while e >= 1:
    print(e * "*") # Done by string concatenation
    e -= 1

# for Loops (Most used)
for i in range(1, 100, 1):
    print(i)

# i = iterator, counter variable
num1 = range(5, 50) # 0 to 49
for i in num1:
    print(i)

# Print even number 1 to 100
# Brute force Formula
for i in range(1, 100):
    if i%2 == 0:
        print(i)

# Efficient Way using range()
# for i in range(start, stop, step) 
for i in range(2, 100, 2):
    print(i)

# Print odd number 1 to 100
# Brute force Formula
for i in range(1, 100):
    if i%2 != 0:
        print(i)

# Efficient Way using range()
# # for i in range(start, stop, step)  
for i in range(1, 100, 2):
    print(i)

#Times table of 3
for i in range(3, 30, 3):
    print(i)

#Times table of 5
for i in range(5, 50, 5):
    print(i)

#Times table of 10
for i in range(10, 100, 10):
    print(i)

#Times table of 99
for i in range(99, 990, 99):
    print(i)

# Use break & continue
# break means stop the process
# continue means skip the process

# Multiplication of 3 [1 to 50] without 21 & break 36
for i in range(1, 51):
    if(i == 21):
        continue
    if(i == 36):
        break
    if(i%3 == 0):
        print(i)

