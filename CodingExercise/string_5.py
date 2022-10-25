# Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

str_1 = 'Hello'
result_str = ''
for letter in str_1:
    result_str = result_str + letter*3
print(result_str)

def paper_doll(str_2):
    result = ''
    for char in str_2:
        result = result + char * 3
    return result


