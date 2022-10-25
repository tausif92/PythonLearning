# str_1 = "Print every word of this sentence that has an even number of the letters"
str_1 = "Print every word of this sentence that has an even number of the letters"

for word in str_1.split():
    if len(word) % 2 == 0:
        print(word)

# Using list comprehension
my_list = [word for word in str_1.split() if len(word) % 2 == 0]
print(my_list)
