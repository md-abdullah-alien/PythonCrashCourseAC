# Question-01:
# Take price of 3 products as input(eg -99.5, 23.75, 16.15). Print total amount & average price
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
sum = x + y + z
average = sum/3
print("Total Amount is: ", sum)
print("Average is: ", average)

# Question-02:
# Take a superhero name as input & check if it starts with 'S' / 's' or not
name = input("Enter Superhero Name: ")
print(name.find('S'))
print('S' in name)
print(name.find('s'))
print('s' in name)