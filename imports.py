"""
Use compounding interest rates and initial investment to find your return on investment
and calculate the taxes owed
"""

import interest # method 1 (i.e. import.annual_interest)
from interest import annual_interest, TAX_RATE # method 2 (i.e. annual_interest)

# TODO: Section 1
# Import the annual_interest and TAX_RATE constants from the file "interest.py" in
# studentrepository/todos/1_basics
# Ask a user how much they would like to invest with an input. Set it equal to a variable
# named "investment".
# TIP: Don't forget to convert the input to an integer!

investment = int(input("What was your revenue this year?"))

# Calculate how much their investment would appreciate in one year by multiplying
# the investment variable by the annual_interest. Set the appreciation amount
# equal to a variable named "appreciation".

appreciate = investment * annual_interest

# TODO: Section 1.1

# Create a new variable named "new_value" by adding the "appreciation" variable to the
# "investment" variable.
new_value = appreciate + investment

# Calculate the taxes you have to pay by setting a variable of "taxes" equal to
# the "appreciation" variable times the TAX_RATE.
taxes = appreciate * TAX_RATE

# Print to the user the following output using f shorthand: "Your investment of {investment} is now worth
# {new_value} and you owe {taxes} in taxes."

print(f"Your investment of {investment} is now worth {new_value} and you owe {taxes} in taxes.")