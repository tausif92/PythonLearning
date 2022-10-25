# Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

str_1 = 'I am home'
words_list = str_1.split()
words_list.reverse()
result = " ".join(words_list)
print(result)

def master_yoda(str_2):
    list_1 = str_2.split()
    list_1.reverse()
    return " ".join(list_1)

# OR

def master_yoda_1(text):
    return ' '.join(text.split()[::-1])

print(master_yoda_1('We are ready'))
