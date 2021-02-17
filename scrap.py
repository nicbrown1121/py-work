import random
# You can import data or functions from files that you yourself defined. In this folder theres a
# file called importable_stuff.py . Let's import the file and use things from it. As you learned in
# Section 1, below is the most straight forward way to import a file.
import importable_stuff

# Then, to access the constant `DAYS_OF_WEEK` from that file,
# you would do so with "dot notation" just like in section 1. In this import case,
# we can find the constant by using:
print(f"Normal dot notation: {importable_stuff.DAYS_OF_WEEK}")

# You could also rename imports such as:
import importable_stuff as stuff # Now this import can be referred to going forward as "stuff".
print(f"Renaming as stuff: {stuff.DAYS_OF_WEEK}")