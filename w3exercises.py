print("Hello, World!") # Command for Printing a statement
import sys
print(sys.version) # Version of python

#Python uses indentation to indicate a block of code.
if 7 > 2:
  print("Seven is greater than two!")

# The number of spaces depends on the programmer
# the most common use is four, but it has to be at least one.
if 7 > 2:
  print("Seven is greater than two!")
if 7 > 2:
     print("Seven is greater than two!")

#the same number of spaces to be used in the same block of code,
# otherwise Python will give  an error
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")

#Python variables
#Python has no command for declaring a variable.
#A variable is created the moment we first assign a value to it.

x = 5
y = "Bob"
print(x)
print(y)

#If we want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#String variables can be declared either by using single or double quotes:
x = "Bob"
# is the same as
x = 'Bob'

#Variable names are case-sensitive.
a = 6
A = "Ray"
#A will not overwrite a

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name
# like (age, carname, total_volume).
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Output Variables
#The Python print() function is often used to output variables.
#In the print() function, we can output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# We can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Prints the data type of the variable x:
x = 5
print(type(x))

#data types
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#There are three numeric types in Python:

#int
#float
#complex
x = 5    # int
y = 5.8  # float
z = 5j   # complex
print(type(x))
print(type(y))
print(type(z))






