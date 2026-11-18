# Topics of Chapter Three
# 01. Arithmetic Operators
# 02. Comparison Operators
# 03. Logical Operators
# 04. Conditionals (if-else)
print("Welcome to Chapter Three")

# Operant (Operator) Operant
# 2 + 2
# Arithmetic Operators ( + , - , * , / )
print(10 + 5) # Addition Operation
print(10 - 5) # Subtraction Operation
print(10 * 5) # Multiplication Operation
print(10 / 5) # Division Operation
print(10 % 5) # Modulo Operation
print(5 ** 3) # Power Operator

# Shortcut Operators (Assignment Operators)
# Addition Operation
a = 1
a += 10 # Output: 11
print(a)

# Subtraction Operation
b = 2
b -= 1 # Output: 1
print(b)

# Multiplication Operation
c = 3
c *= 10 # Output: 30
print(c)

# Division Operation
d = 4
d /= 2 # Output: 2
print(d)

# Modulo Operation
e = 5
e %= 2 # Output: 1
print(e)

# Power Operator
f = 6
f **= 2 # Output: 36
print(f)

# Mathematical Precedence (Follow BODMAS)
# B — Brackets ( ), { }, [ ]
# O — Orders or Of (powers, square roots, exponents, or calculations labeled "of")
# D — Division (÷)
# M — Multiplication (×)
# A — Addition (+)
# S — Subtraction (-)


# Operator Precedence (BDMAS)
# Brackets ( ) Top Priority
# D — Division (÷)
# M — Multiplication (×)
# &&
# A — Addition (+)
# S — Subtraction (-)

case1 = (2 + 5) * 3
print(case1)

case2 = 2 + 5 * 3
print(case2)

# If operators is same precedence they get priority LEFT to RIGHT order
case3 = 2 + 3 * 4 - 8 / 2
# Step-01: 2 + 3 * 4 - 8 / 2
# Step-02: 2 + 12 - 4
# Step-03: 14 - 4
# Step-04: 10 
print(case3)

# Comparison Operator
# >(Greater than)
# <(Less than)
# >=(Greater than or equal)
# <=(Less than or equal)
# ==(Equal to)
# !=(Not Equal to)
# =(Assignment Operator) ==>Assign value right to left

print(3 > 2) # True
print(3+7 > 2+8) # False
print(3+7 >= 2+8) # True
print(3 < 2) # False
print(3-1 < 2+3) # True



# Logical Operators (or, and, not)
# or ==> One True == Overall True
# and ==> One False == Overall False
# not ==> 

statement1 = 3 > 5 # False
statement2 = 3 > 2 # True
statement3 = 5+10 > 11 # True
print(statement1 or statement2) # Overall True
print(statement1 and statement2) # Overall False
print(not statement1) # Overall True
print(not statement3) # Overall False

# Conditionals Statement (if-else/if-elif-else)
age = int(input("Enter your age:"))
# Indentation(:)==> Means proper gapping. Every condition give a semicolon then give a gap of size tab/space of 4 times
if age >= 18 and age <= 70:
    print("You are an adult & Must be alive.")
elif age < 18 and age > 0:
    print("You are a child & Must be born")
elif age > 70:
    print("May be RIP")
elif age < 0:
    print("Born first")
else:
    print("You are not Human")

print("End of code")

marks = int(input("Enter Your Marks: "))
if marks<=100 and marks>=80:
    print("You got A")
    print("Keep it up!!!")
elif marks<80 and marks>=60:
    print("You got B")
    print("Try harder to best!!!")
elif marks<60 and marks>=0:
    print("You got C")
    print("You should do hard work..!")
else:
    print("Error! Invalid input")

