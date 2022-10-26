# Tuples are similar to list except that tuples are immutable
tuple_1 = (1, 6, 2, "Tausif", 5, 1)
print(f"Original Tuple: {tuple_1}")

print(f"Tuple length: {len(tuple_1)}")

# Get item at specific index
print(f"Item at 1st index: {tuple_1[1]}")

# Get the count of a specific item in tuple
print(f"Number of occurrences of 1: {tuple_1.count(1)}")

# Get the index of a specific item in tuple
print(f"Index of 1st occurrence of 1: {tuple_1.index(1)}")

# Tuple unpacking
list_of_tuples = [("Apple", 60), ("Mango", 80), ("Banana", 20)]
# To get the price of the apple, Mango and Banana, we can use tuple unpacking
for fruit, price in list_of_tuples:
    print(fruit)
    print(price)

