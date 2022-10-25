# *args is used to receive any number of arguments in tuple which we can iterate over in the function
# **kwargs is the keyword arguments used to receive any number of arguments which we can iterate over in the function

def my_func(*args, **kwargs):
    for item in args:
        pass
    for key in kwargs.keys():
        pass
    for value in kwargs.values():
        pass

######## maps #############
# Imagine you have a function below
def square(num):
    return num**2

# And you want to call this function on an iterable object i.e. list or tuple
my_nums = [1,2,3,4,5,6,7,8,9,10]
for item in map(square, my_nums):   # map(square, my_nums) returns <map at some_memory_location>
    # we need to iterate to get values
    print(item)

# OR we can convert it to list
print(list(map(square, my_nums)))  # Note that we are pointing to the function, but we are not calling it like "square()"

######## filter #############
def check_even(num):   # To use filter, function has to return boolean True or False
    return num % 2 == 0

my_nums = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even, my_nums)))

######## lamda #############
# lamda functions are anonymous functions which are basically one time use and does not have a func name.
# This can be very handy when we have a small function and we are not going to use again
square = lambda num: num**2
print(square(5))

# Now, the map and filter functions requires the small functions to be predefined. Instead of defining the functions separately,
# we can use lamda expressions
print(list(map(lambda num: num ** 2, my_nums)))

# Same goes with filter function
print(list(filter(lambda num: num % 2 == 0, my_nums)))
