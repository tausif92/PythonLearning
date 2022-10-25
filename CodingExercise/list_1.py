# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(list_1):
    for i in range(0, len(list_1) - 1):
        if list_1[i] == 3 and list_1[i+1] == 3:
            return True
    return False

print(has_33([3,1,2,3,4,3]))

