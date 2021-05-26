
def addTwo(j):
    newNum = j + 2
    return newNum # Control 3: "j", which is equal to the argument of 9 that was passed, has 2
                  # added to it and 11 is returned.

added_two = addTwo(3)
print(f"We called 'addTwo' and set it's return value equal to a variable. That variable equals {added_two}")


math_classes = [
    {
        'subject': 'Math',
        'level': 'Geometry',
        'teacher': 'Professor Alisson',
        'students': ['Bill', 'Bob', 'Beatrice', 'Brandi'],
        'averages': {
            'MP1': 89.5,
            'MP2': 82,
            'MP3': 92,
            'MP4': 94,
        }
    },
    {
        'subject': 'Math',
        'level': 'Algebra',
        'teacher': 'Professor Dylan',
        'students': ['Callie', 'Chris', 'Cayla', 'Chantelle'],
        'averages': {
            'MP1': 95,
            'MP2': 86,
            'MP3': 97,
            'MP4': 79,
        }
    },
    {
        'subject': 'Math',
        'level': 'Calculus',
        'teacher': 'Professor Johnson',
        'students': ['Dani', 'Damien', 'Dinesh', 'Dira'],
        'averages': {
            'MP1': 99,
            'MP2': 86,
            'MP3': 77,
            'MP4': 94.8,
        }
    },
]
# Lets see how to find the entire dictionary for the Calculus course. To do so, we 
# will set up a for loop with a conditional statement in it to test which level 
# we are iterating over. Then we can go ahead and print the entire calculus dictionary,
# also known as 'math_classes' third key

for key in math_classes:
    level = key["level"]
    if (level == "Calculus"):
        print(key)

    def daysActivities(type_of_day):
        if (type_of_day == "fun"):
            day_string = "You should enjoy some of your favorite activities."
        else:
         day_string = "You should try to have some more fun!"
    return day_string 

def daysActivities(type_of_day):
    """Analyze a user's input and return a message for them. Just as a file gets a doc string,
    functions get one too!"""
    # The conditionals below check to see if the "type_of_day" argument is equal to something. In
    # our case we are a conditional statement to determine if "type_of_day" is "fun". If the
    # conditional is true, then whatever is within the scope of the conditional is executed. If the
    # conditional is not true, the "else" block's code is executed.

    if (type_of_day == "fun"):
        day_string = "You should enjoy some of your favorite activities."
    else:
        day_string = "You should try to have some more fun!"
    
    return day_string # This will return the variable "day_string" and end the function. When a return
                      # statement is run, the function will effectively stop running.

def inquireDay():
    """This function will ask the user what type of day they want to have"""

    # First we will take the user input value and then pass it as an argument to our
    # "daysActivities()" function.
    user_day = input("What type of day do you want to have? You can choose 'fun' or a response of your own. Enter your choice: ")

    user_message = daysActivities(user_day)
    print(user_message) # The variable "user_message" will be equal to the return value of the
                        # function call.

inquireDay() # This is a standard function call without any parameters.