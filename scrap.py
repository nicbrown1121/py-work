grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

# When you use a "for loop" with a dictionary, the variable gets set to every key, but not the value.
for student in grades:
    print(f"{student} got a {grades[student]} on their comp sci exam.")
    
print("\n2nd for loop:\n")
for student in grades:
    grade = grades[student]
    print(f"{student} got a {grade} on their comp sci exam.")

