# 6.57 Notes - Defining and Calling Python functions
print("Hello")
num_char = len("Hello")
print(num_char)


# make our own function
def my_function():
    print("Hello")
    print("Bye")


my_function()

# recap
# def my_function():
#   do this
#   then do this
#   finally do this

# 6.59 Notes - Indentation in Python
# https://www.python.org/dev/peps/pep-0008/
# use 4 spaces, not tabs. if possible, utilize the IDE to treat tabs as 4spaces.

# # 6.60 While Loops
# # while something_is_true:
# #   Do something repeatedly.
# # from previous exercise, we could do
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
