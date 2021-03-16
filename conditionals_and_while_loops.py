"""
Expanding on loops
"""

# TODO: Section 1.1:

# Write a program that takes a user input of an integer and store it in a variable called
# "user_int". If the integer is even, print the statement "[user_int] is even.". Otherwise, print
# the statement "[user_int] is odd."
# TIP: Remember modulo from the Basic Math lesson?
# TIP: Consider how that can help us identify odd/even numbers.

user_int = int(input("Enter a number: "))
if (user_int % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")

####################################################################################################

# TODO: Section 2.1
# Write a while loop that iterates through the list "todos". For each iteration, remove an item
# using the ".pop()" method and append it to the list "finsihed_todos". Keep track of all of your
# finished todos by printing "finished_todos" in each iteration.

todos = ["exercise for fun", "eat food", "go to school", "write some code"]
finished_todos = []

while todos:
    task = todos.pop()
    finished_todos.append(task)
    print(f"finished todo list: ", finished_todos)

####################################################################################################

# TODO: Section 2.2

# Write a while loop that increases "var" by increments of 2 until "var" is greater than or equal to
# 21. Note the wording of this question and set the condition appropriately. Print "var" in each
# iteration.

var = 7

while (var < 21):
    var = var + 2
    print(var)

####################################################################################################

# TODO: Section 2.3

# Write a program that takes a user input of an integer and store it in a variable called
# "user_int". Write a loop with this integer as the condition and test if "user_int" is even.
# If "user_int" is even, increment "user_int" by 1. Otherwise, decrement "user_int" by 3.
# Then print "user_int" for each iteration.

# Important:
# For the purpose of this exercise please input only POSITIVE integers.

user_int = int(input("Enter an integer: "))
if (user_int % 2 ==0):
    user_int = user_int + 1
    print (user_int)
else:
    user_int = user_int - 3
    print (user_int)

