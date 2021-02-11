"""
Using variables and types
"""

# TODO: Section 1:
# Set a variable 'phrase1' euqal to "Hi everyone! " and another variable 'phrase2'
# equal to "My name is [name here]". Then use what you learned so
# far in the lesson to set these varibles to a new variable called "complete"
# and print it.
phase1 = "Hi Everyone!"
phase2 = "My name is Nicole"
print (phase1 +" " + phase2)

####################################################################################################

# TODO: Section 2:
# Set two variable in the same line, "flt1" and "flt2", equal to 3.5 and 14.0, respectively.
# Then print each variable to check the output.
flt1, flt2 = "3.5", "14.0"
print (flt1 + " " + flt2)

####################################################################################################

# TODO: Section 3:
# Set a variable called name equal to your name, then set a variable of age
# equal to your age as an integer. Print a statement with an output of
# "My name is [name here] and I am [age here] years old." using the above
# variables in your print statement.
name1 = "Nicole"
age1 = int(26)
print ("My name is", name1, "and I am ", age1, " years old")

# Takeaway:

# Concatenation (+) can only be done with strings, not strings and integers/floats. Commas, however,
# simply print different elements rather than attempting to concatenate strings.

####################################################################################################

# TODO: Section 4:
# Set a variable equal to each of the types we have learned so far. That includes
# integers, floats, booleans, None, and strings. So, have one variable per each
# of those types (i.e. exampleInt = 0, exampleBool = False, etc.).
# To check the type of something in python, you use the type() function.
# For example, type("Hello") would yield string, and type(6) would yield int.
# So, create on print statement that would print the type of each variable you've set.
int1, string1, float1, boolean1, string2 = 2, "My name is Nicole", 12.98, True, None
print (type(int1))
print (type(string1))
print (type(boolean1))
print (type(string2))
print (type (float1))


# Takeaway:
# Types are important in Python and you can check different elements' types using type().
# The type() function is an example of a polymorphic function, meaning that the same
# function name can be used for different types.

####################################################################################################

# TODO: Section 5:

# Lastly, we will introduce type conversion. There are functions you can use to
# convert things in Python. The first type conversion function we will use is str().
# Try the problem from Section 3, but use plus signs to concatenate strings and
# print "My name is [name here] and I am [age here] years old." using the name and age
# variables. However, this time when you're concatenating the age variable, wrap it in the
# str() function as such: str(age). The print statement will no longer throw an
# error 🎯 since age was converted to a string.
name2, age2 = "Nicole", 26
print("My name is " + name2 + " and I am " + str(age2) + " years old.")
# Takeaway:
# We can change types in Python when appropriate, and we learned one way to do so with str()

# Good job, everyone! First todo down 💪🏾
