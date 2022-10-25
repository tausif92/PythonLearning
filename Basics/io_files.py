# Open file
my_file = open("my_test_file.txt")

# Read the contents of the file
print(my_file.read())

# When the file is read, you cannot read it again because the curser is at the end of the file.
# To read it again, you need to seek the curser to the beginning
my_file.seek(0)
print(my_file.read())

# To read line and print each line in the list. If the file is already read, bring the curser to 0
my_file.seek(0)
print(my_file.readlines())

# Close file
my_file.close()

# File modes
# mode='r' --> read only
# mode='w' --> write only (overwrite or create new)
# mode='a' --> append only (add on to files) - cursor is at the end
# mode='r+' --> read and write
# mode='w+' --> read and write (overwrite or create new)

# Write in file
my_file = open("my_test_file.txt", mode='a')
my_file.write("Place: Bangalore\n")
my_file.close()

my_file = open("my_test_file.txt", mode='r')
print(my_file.read())
