import random

# Set the percentage of True and False
percent_true = 0.75
percent_false = 1 - percent_true

# Generate the list
random_bool_list = random.choices([True, False], weights=[percent_true, percent_false], k=10)
print(random_bool_list)