# Lecture #37 is very imp from udemy course
# Duplicate keys are not allowed. Once key1 is assigned, if key1 is set again in the dictionary like below,
# it will use latest key1 value, which is value5
# dict_1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key1": "value5"}

dict_1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5"}
print(f"Original dictionary: {dict_1}")

# Get dictionary value using key
print(f"Value with key1: {dict_1['key1']}")

# Update dictionary
dict_1['key5'] = 'Updated value'
print(f"Dictionary after update: {dict_1}")

# Get dictionary keys
print(f"Dictionary keys: {dict_1.keys()}")

# Get dictionary values
print(f"Dictionary values: {dict_1.values()}")

# Get dictionary items
print(f"Dictionary items: {dict_1.items()}")

dic = {"a":10, "b":20}
print(dic.get("c", "No key found!"))  # returns value if the key is present in dict else returns None. Does not fail
# Message can also be customized if the key is not found

print(dic["a"])  # returns value if the key is present in dict else fail with KeyError
