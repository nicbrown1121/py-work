number_list = [3, 15, 31, 1, 11, 107]

# `enumerate` gives you the index position and actual value of the items in a list
for number in enumerate(number_list):
    print(number) # enumerate returns you a tuple in the form of (index, value). Remember- tuples are
                  # lists that cannot be changed!
    print(number[0]) # this will be the index number
    print(number[1]) # this will be the item