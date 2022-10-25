# Sets are unordered collection of unique elements. It will not fail to add duplicate items,
# but it removes the duplicate items if it is being added

set_1 = {2, 3, 5, 1, "Tausif"}

print(f"Original set: {set_1}")

# Add elements to set
set_1.add(9)
print(f"Updated set: {set_1}")
set_1.add(9)
print(f"Updated set: {set_1}")

# If we have a list with duplicate items and we want to remove the duplicates, we can cast it to set
list_1 = [1, 2, 3, 1, 3, 2, 1]
print(f"Set of the list {list_1} is: {set(list_1)}")

