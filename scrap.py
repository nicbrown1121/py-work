programming_languages = {"lang_one": "Python", "lang_two": "Java"}
print(programming_languages)

# Here you can see that the len() function calculates the number of key/value pairs in a dictionary.
print(f"The programming language dictionary's length is {len(programming_languages)}")
programming_languages["lang_three"] = "CSharp"
print(f"After adding a key/value pair: {programming_languages}")
programming_languages["lang_two"] = "Golang"
print(f"post golang {programming_languages}")


lang_two = programming_languages.pop("lang_two")
print(f"lang_two is equal to: {lang_two}")
print(f"post pop 2: programming_languages is equal to: {programming_languages}")

# The get method will find a value for a key in a dictionary.
example_dict = {"num_one": 10, "num_two": 20, "num_three": 30}
second_value = example_dict.get("num_two")
print(second_value)
fourth_value = example_dict.get("num_four")
print(fourth_value)

# You can also specify a return value if the key does not exist in the dictionary.
fourth_value = example_dict.get("num_four", "Does not exist.")
print(fourth_value)