# Topics of Chapter Two
# 01. Type Conversion(Done by Interpreter) & Type Casting(DOne by Programmer)
# ==> str(), int(), float(), bool()
# 02. Sum Program
# 03. String Methods
# 04. Keywords
print("Welcome to Chapter Two")

# Type Conversion ==> Implicit Conversion
print("The value of pi is:", 2 + 1.1416)

# Type Casting ==> Explicit Conversion
print("The value of pi is not:", 2 + int(1.1416))

# Type One ==> Type casting then print 
age1 = input("Enter Your Age: ")
print("Your entering age is:",  age1 , "& Which type is:", type(age1))
age1 = int(age1)
age1 = age1 + 10
print("Updated age is:", age1)
print("Floating Value age is: ", float(age1))

# Type Two ==> Type casted user input
age2 = int(input("Enter Your Age: "))
print("Your entering age is:",  age2 , "& Which type is:", type(age2))
age2 = age2 + 10
print("Updated age is:", age2)
print("Floating Value age is: ", float(age2))

# Type Three ==> Type casted user input + values
age3 = int(input("Enter Your Age: ")) + 10
print("Your entering updated age is:",  age3 , "& Which type is:", type(age3))
print("Floating Value age is: ", float(age3))

# Sum Program ==> a, b ==> sum
a = int(input("Enter a: "))
b = int(input("Enter b: "))
sum = a + b
print("Sum is: ", sum)

# Subtraction Program ==> c, d ==> subtraction
c = int(input("Enter c: "))
d = int(input("Enter d: "))
subtraction = c - d
print("Subtraction is: ", subtraction)

# Multiplication Program ==> e, f ==> multiplication
e = int(input("Enter e: "))
f = int(input("Enter f: "))
multiplication = e * f
print("Multiplication is: ", multiplication)

# Division Program ==> g, h ==> division
g = int(input("Enter g: "))
h = int(input("Enter h: "))
division = g / h
print("Division is: ", division)

# Modulus Program ==> i, j ==> modulus
i = int(input("Enter i: "))
j = int(input("Enter j: "))
modulus = i % j 
print("Modulus is: ", modulus)

name = "Md Abdullah" # string
grade = 'A'

# String Operation ==> Not change any main operation
# Python strings are IMMUTABLE (cannot change)
print(name) # string
print(name.upper()) # New string
print(name.lower()) # New string

# Find(find() operation) something ==> index/position return
print(name.find("u")) # return 6 means true
print(name.find("ll")) # return 7 means true
print(name.find("a")) # return 9 means true
print(name.find("j")) # return -1 means false

# Replace something ==> Replace 
print(name.replace("Md", "MD"))
print(name.replace("Abdullah", "ABDULLAH"))
print(name.replace("Md Abdullah", "MD ABDULLAH"))
# print(name.replace("Abdullah", name.upper()))

# Check for presence ==> Find substring exit or not exit in string
print('M' in name) # Exited in 'Md Abdullah' ==> return True
print('d' in name) # Exited in 'Md Abdullah' ==> return True
print('D' in name) # Not Exited in 'Md Abdullah' ==> return False
print('B' in name) # Not Exited in 'Md Abdullah' ==> return False

# Keywords means reserved word in programming language dictionary
# Some keywords: in, True, False, while, for, break, continue
True = "abcd" # Give an error because True is a keyword
abcd = "abcd" # Give not error because abcd is normal variables