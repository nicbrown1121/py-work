"""
Working with functions and scope
"""

# TODO: Section 1:
# Define a function called "double" that sets a parameter of x. It should double x and
# print that value. Call the function and pass it the below variable as an argument.
double_this = 7
def double(x):
    return x * 2
print(double(double_this))

# After completing the above, define a function called "printer", that sets no parameter.
# The function should just print the "double_this" variable. Call the function.

def printer():
    print(double_this)
print("Calling printer:")
printer()

####################################################################################################

# TODO: Section 2:
# Copy your "doubled" function from above to this block of code. Change it to use a return value,
# store that return value in a variable, and print it.
double_this = 3
def double(x):
    newNum = x * 2
    return newNum
print(double(double_this))

newNum = double(double_this)

####################################################################################################

# TODO: Section 2.1:
# Write an if statement that prints "[number here] is even" if the above functions return value
# is even. Write an additional if statement that prints "[number here] is odd" if it is odd.
 
if(newNum % 2 == 0):
    print(f"{newNum} is even")

####################################################################################################

# TODO: Section 3:
# Create a function that takes a dictionary as an argument, loops through the
# dictionary, then returns the iteration number, key, and value in a readable way.
# (i.e. "iteration number 1 returns the key firstKey and the value firstValue")

# Here is an example dictionary:
EXAMPLE_DICTIONARY = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}

# Place the function below.
def dictionary_reader(dictionary):
    i = 1
    for key in dictionary:
        print(f"Iteration {i} returns the key {key} and the value {dictionary[key]}")
        i= i+1
dictionary_reader(EXAMPLE_DICTIONARY)
