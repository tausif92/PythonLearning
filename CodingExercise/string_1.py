# str_1 = "Print only the words that starts with s in the sentence"
str_1 = "Print only the words that starts with s or S in the Sentence"
my_list = []
words_list = str_1.split()
for word in words_list:
    if word[0].lower() == "s":
        my_list.append(word)
print(my_list)

# The above code can also be done with list comprehension
my_list_1 = [word for word in str_1.lower().split() if word[0] == "s"]
print(my_list_1)

# The above code can also be done with list comprehension
my_list_2 = [word for word in str_1.lower().split() if word.startswith("s")]
print(my_list_2)

