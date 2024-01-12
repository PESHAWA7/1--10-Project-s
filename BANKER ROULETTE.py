import random

names_string = input("names : ")
names = names_string.split(" ")

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[1])
