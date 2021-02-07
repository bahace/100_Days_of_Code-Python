# # 4.39 psuedo random numbers
# # import random module
# import random
# # assign a random integer to the variable
# random_integer = random.randint(1, 10)
# print(random_integer)
# # random float 0.0 - 0.999999
# random_float = random.random()
# print(random_float)
# # what if we want a random float between 0.0 - 5.0?   use multiply
# random_float1 = random.random()
# random_float1 *= 5
# print(random_float1)

# # 4.41 Understanding the offset and appending items to lists
# # lists URL https://docs.python.org/3/tutorial/datastructures.html
# fruits = ["Chery", "Apple", "Pear"]
# us_states = ["Texas", "New York", "Florida"]
# # print the X item in the list
# print(us_states[2])
# # Can also count negative, starts from end of list
# print(us_states[-2])
# # Alter an item in the list
# us_states[2] = "Oklahoma"
# print(us_states[2])
# # add an item at the end of a list
# us_states.append("Davisland")
# print(us_states)
# # extend list - add more then 1 item to it
# us_states.extend(["Brattland", "Redland"])
# print(us_states)

# 4.43 IndexErrors and Working with Nested Lists
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]
# how can list out within our current list the fruits and vegetables?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][2])
