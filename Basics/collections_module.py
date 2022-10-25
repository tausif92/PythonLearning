from collections import Counter

# To count the number of occurrences of each item in a list
list_1 = [1,1,1,2,2,2,2,3,3,3,4,5,4,6]
print(Counter(list_1))  # Counter returns the dict key value pairs where key is the item and value is the no. of occurrences

# Get unique list of items from list_1: [1, 2, 3, 4, 5, 6]
print(list(Counter(list_1)))

list_2 = ['a','b','a','b','a','b','a','b', 1, 1, 2]  # works with list of numbers and string
print(Counter(list_2))

print(Counter("aaabbbjshhhsjj"))

