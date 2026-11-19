# Topics of Chapter Six
# 01. Functions
# 02. In-built Functions
# 03. Module Functions
print("Welcome to Chapter Six")

price1 = 100
new_price1 = price1 + price1*0.18
print(new_price1)

price2 = 70
new_price2 = price2 + price2*0.18
print(new_price2)

price3 = 50
new_price3 = price3 + price3*0.18
print(new_price3)
# It occurs data Redundancy problem

# Create a function which calculate two numbers
# Using 'def' means function define. It void types
def sum1(a, b):
    print("Sum is: ", a+b)

# Function call/use 'sum(value of a, value of b)
# In void type, we should just call the function, not needed to print it.
sum1(100,200)

# Using 'def' means function define. It return type
def sum1(a, b):
    return a+b

# Function call/use 'sum(value of a, value of b)
# In return type, we should call the function in print function.
print("Sum is: ", sum1(10,5))

# Function Define with return
def calculate_GST(p): # Here 'p' is called parameters
    new_p = p + p*0.25
    return new_p

# Function Call
print(calculate_GST(100)) # Here value is called arguments
print(calculate_GST(200))
print(calculate_GST(300))

# Arguments store into parameters when we call a function

# Function Define without return
def calculate_GST(p): # Here 'p' is called parameters
    new_p = p + p*0.20
    print(new_p)

# Function Call
calculate_GST(300) # Here value is called arguments
calculate_GST(200) 
calculate_GST(100) 

# There are two types of function
# 01. User define function. Means function is created by user.
# 02. In-built function. Means function is created by built-in.
# 03. Module Function. It is collection of related function.
# In python, module means when we create a bundle or collection of something.

# Example of User Define Function:
# Function Create
def multiplication(a, b):
    print("Multiplication is: ", a*b)

# Function Call
multiplication(10,5)

# Example of In-built Function:
print("Hello World")
print(len([10, 20, 30, 40, 50]))
print(min(10, 20, 30, 40, 50))
print(max(10, 20, 30, 40, 50))
print(type([10, 20, 30, 40, 50])) # Mutable
print(type({10, 20, 30, 40, 500})) # Mutable
print(type((10, 20, 30, 40, 500))) # Immutable

# Module Function
import math # Added a math module
print(dir(math)) # Show directory of math module

# Example-01
from math import sqrt, log2 # Added square-root module
print(sqrt(16))
print(log2(16))

# Example-2
import random
print(random.random) # It print random locations
print(random.random()) # It print random values 0 to 1
print(random.randint) # It print random range locations
print(random.randint(1, 20)) # It print random range value a to b

