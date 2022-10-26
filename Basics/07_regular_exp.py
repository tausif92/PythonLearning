import re

raw_str = "12 This is my phone number: 9999977776 and this is my email: user@email.com. You can reach out on my phone or email. 2"

pattern1 = "phone"

# Returns None if match is not found. Returns only the first match found
print(re.search(pattern1, raw_str))  # match found --> <re.Match object; span=(11, 16), match='phone'>

# Returns all the matches in the text
print(re.findall(pattern1, raw_str))  # Returns the list of matches
# We can find the number of occurrences of matches by using builtin len() function
print(len(re.findall(pattern1, raw_str)))

# Find phone number
print(re.search(r"\d{10}", raw_str))   # <re.Match object; span=(25, 35), match='9999977776'>
# OR
print(re.findall(r"\d{10}", raw_str))  # ['9999977776']

# Find email
print(re.search(r"\w+@\w+.com", raw_str))  # <re.Match object; span=(58, 72), match='user@email.com'>
# OR
print(re.findall(r"\w+@\w+.com", raw_str))  # ['user@email.com']

# Using OR |
print(re.search(r"phone | mobile", raw_str))  # This will look for phone or mobile in the string

# Using wild card .
print(re.search(r"ph.ne | .obile", raw_str))  # This will look for phone or mobile in the string using .

# Using wild card starts with ^
print(re.findall(r"^\d", raw_str))   # This will search if the entire raw string starts with a number

# Using wild card ends with $
print(re.findall(r"\d$", raw_str))

# Exclude numbers using []
print(re.findall(r"[^\d]+", raw_str))

