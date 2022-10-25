# Strings are immutable. That means once you assign a value to a string variable, you cannot update it unlike lists.
# Eg. str_1[0] = "T" --> This will give error that strings are immutable
import string

str_1 = "hello woRld!"
print("Original string: " + str_1)

print(len(str_1))
# String indexing is used to grab a character at a particular index
first_char = str_1[0]
last_char = str_1[-1]

# String slicing is used to grab the multiple characters by giving the starting and finishing index
# str_1[starting_index, finishing_index, step_size]
slice_1 = str_1[2:]   # llo World!
slice_2 = str_1[2:7]  # llo W
slice_3 = str_1[:7]   # Hello W
slice_4 = str_1[::2]  # HloWrd

# String concatenation
concat = "This is an example of concatenation:" + slice_1 + slice_2

# Count number of occurrences of letter "l":
print("Number of occurrences of l is: " + str(str_1.count("l")))

# Find index of the first occurrence of a character. Returns -1 if the char is not found.
print("Index of w (first occurrence) in the string is: " + str(str_1.find("w")))

# Capitalize string
print("Capitalized string is: " + str_1.capitalize())

# Returns boolean True if the string is in lower case else returns False
print("Is string in lower case: " + str(str_1.islower()))

print("Is string in upper case: " + str(str_1.isupper()))

print("String in upper case: " + str(str_1.upper()))

print("String in lower case: " + str_1.lower())

print("Replace o with O: " + str_1.replace("o", "O"))

print("Splits by white spaces: " + str(str_1.split()))

print("Splits by character l: " + str(str_1.split("l")))

# Format string
print("The {} can {}.".format("dog", "bark"))

print("Round off 3 decimal places: {decimal_number:1.3f}".format(decimal_number=104.12345))

# New formatting syntax
print(f"The string is: {str_1}")

# Get all the alphabets (a-z) in lower case
print(set(string.ascii_lowercase))
