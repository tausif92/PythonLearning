
list_1 = [1, 5, 2, "Tausif", 4.54]
print(f"Original list: {list_1}")
# Get length of the string
print(f"\nLength of the list is: {len(list_1)}")

# Slicing and indexing works same as string
print(f"List item at 0th index: {list_1[0]}")
print(f"List items starting from 2nd index: {list_1[2:]}")
print(f"List items from 2nd to 5th index with step size of 2: {list_1[2:5:2]}")
print(f"List item from 2nd index till end with step size of 2: {list_1[2::2]}")

new_list = ["Bajaria", 3, 1, 9, 0, 4]
print(f"New list: {new_list}")
conctenated_list = list_1 + new_list
print(f"Concatenated list: {conctenated_list}")

# Update item of a list
list_1[0] = 8
print(f"Original list after update: {list_1}")

# Append list item at the end of the list
list_1.append("New Item")
print(f"List after append: {list_1}")

# Remove/pop last item of the list
list_1.pop()
print(f"List after pop: {list_1}")

# Pop at specific index
list_1.pop(0)
print(f"List after pop at 0th index: {list_1}")

# Sorting only works with the same data type items in the list.
# list_1.sort()
# print(f"List after sorting: {list_1}")

list_1.reverse()
print(f"List after reversing: {list_1}")

# Insert the item at the given index
list_1.insert(0, 25)
print(f"List after inserting 25 at 0th index: {list_1}")

# List comprehension is a unique way of quickly and dynamically creating a list with python
# Consider a scenario where you want the string letters to be stored in a list
my_str = "Tausif"
my_list = []
for letter in my_str:
    my_list.append(letter)
print(f"List of letters: {my_list}")

# Use of list comprehension for the above code snippet:
my_list_1 = [letter for letter in my_str]
print(f"List of letters using list comprehension: {my_list_1}")

# Creating list of first 10 integers using list comprehension
my_list_2 = [num for num in range(1, 11)]
print(my_list_2)

# Creating list of square of first 10 integers using list comprehension
my_list_3 = [num**2 for num in range(1, 11)]    # num**2 is same as num to the power 2 or num*num
print(my_list_3)

# Creating list of even numbers of first 10 integers using list comprehension
my_list_4 = [num for num in range(0, 11) if num % 2 == 0]
print(my_list_4)

# Creating list of square of even numbers of first 10 integers using list comprehension
my_list_5 = [num*num for num in range(0, 11) if num % 2 == 0]
print(my_list_5)

# Converting the list of temperature in celcius to fehrenheit
celcius = [21, 23, 30, 45, 32]
fehrenheit = [round(( (9/5)*temp + 32), 2) for temp in celcius]
print(fehrenheit)

# Putting else in list comprehension
my_list_6 = ["even" if num % 2 == 0 else "odd" for num in range(0, 11)]
print(my_list_6)
