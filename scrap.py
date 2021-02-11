squares = [x**2 for x in range(10)] # Each "iteration" of this loop represents a number between
                                    # 0 and 9, which will be named "i". We square the number "i"
                                    # for each iteration and append it to the list, "squares".
print(f"Squares list {squares}")


values = [1, 2, 3, 4, 5, 6]
even = values[0:6:2]
print(even)
# Segment the items in the list "values" to include only the even numbers.
# Save this slice as the variable "even". Then, print the "even" variable.
# HINT: Use a stepper, which would skip every other number)