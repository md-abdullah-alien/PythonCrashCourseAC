# Topics of Chapter Four
# 01. List
# 02. Tuple
# 03. Set
# 04. Dictionary
print("Welcome to Chapter Five")

# Data Types
# Primitive: bool, int, float, string
# Non-Primitive/Complex: List, Tuple, Set, Dictionary

# List: Different types/collection of items. It's mutable
mark1 = [98, 99, 97, 95, 93]
print(mark1, type(mark1))

mark2 = [98, 99, 97, 95, 93, 'A', 92.5]
print(mark2, type(mark2))

# Total Length of List
print(len(mark1))
print(len(mark2))

# Index Value find
print(mark1[1])
print(mark1[0])
print(mark2[5])
print(mark2[6])

# Index value in reverse order
print(mark1[-1])
print(mark1[0])
print(mark2[-5])
print(mark2[-6])

# Slicing a list ==> Cut list into sub parts
# list[start_index:end_index]
# print start_index to end_index-1
print(mark1[0:3]) # index 0 to 2
print(mark1[-3:-1]) # index -3 to -2
# By default staring index 0 and ending index n-1
print(mark1[:]) # Default value takes total list
print(mark1[:3]) # index 0 to 2
print(mark1[3:]) # index 3 to 4

for score in mark1:
    print(score)

# If I want to add a value in last of the list
# append(index position, value)
# append default index position last index
mark1.append(50)
print(mark1)

# Find elements exist or not
print(97 in mark1)
print(50 in mark1)
print(100 in mark1)

# If I want to clear my list
print(mark1.clear())

# For check the length of the list
print(mark1, len(mark1))

# Tuple behave like list but it's Immutable
mark3 = (98, 99, 97, 95, 93)
mark4 = 98, 99, 97, 95, 93, 95, 95 # Not must needed parenthesis

print(mark3, type(mark3))
print(mark4, type(mark4))

# Show element of a tuple
print(mark3[2])
print(mark3[-1])
print(mark3[3])

# Count any elements of a Tuple
print(mark4.count(95)) # Count the repeated value in the tuple
print(mark4.index(95)) # Position of index value

# Try to add some value in tuple. It's total impossible
#mark4[0] = 100 # Give an error

# Set ==> Unique items collection
marks5 = {98, 97, 95, 96, 95, 96}
print(len(marks5)) # length is 4
print(marks5)

# Showing set & set elements
for score in marks5:
    print(score)

# Dictionary key && value parare ==> It's mutable
marks6 = {"Math:": 99, "Physics:": 97, "Chemistry:": 98}
print(marks6, type(marks6))

marks6["Physics:"] = 95
print(marks6["Physics:"]== 95)

marks6["English:"] = 75
print(marks6["English:"])

for key in marks6:
    print(key, marks6[key])

# Immutable is faster than mutable data types
# Mutable data:
# Immutable data: Tuple