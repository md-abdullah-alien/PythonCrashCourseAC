# Question-01:
# Write a Function (WAF_1) to check if a number is odd or even
def WAF_1(a):
    if(a%2 == 0):
        print("Even Number")
    else:
        print("Odd Number")
a = int(input("Enter a number to check Even or Odd check: "))
WAF_1(a)

# Question-02:
# WAF_2 to count the number of vowels in a string
def WAF_2(text):
    counter = 0
    for s in text:
        if(s == 'A' or s == 'a' or s == 'E' or s == 'e' or s == 'I' or s == 'i' or s == 'O' or s == 'o' or s == 'U' or s == 'u'):
            counter+=1
    print(counter)

text = input("Enter a text to count vowels: ")
WAF_2(text)

# Question-03:
# WAF_3 to print if a number is prime or not
import math
def WAF_3(num):
  if num <= 1:
    print("Not Prime Number")
    return
  for i in range(2, int(math.sqrt(num)) + 1):
    # Check if num IS divisible by i
    if num % i == 0:
      print("Not Prime Number")
      break  # Stop checking immediately once a divisor is found
  else:
    # This runs ONLY if the loop finishes without hitting 'break'
    print("Prime Number")

num = int(input("Enter a number to check prime or not prime: "))
WAF_3(num)

# Question-04:
# WAF_4 to return the average marks if a list of marks is passed as parameter
import math
def WAF_4(marks):
   total = 0
   counter = 0
   for m in marks:
      total += m
      counter += 1
   average = total/counter
   print("Average is: ", average)

marks = (10, 20, 30, 40, 50)
WAF_4(marks)
