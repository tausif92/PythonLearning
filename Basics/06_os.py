import os
import shutil

# Get current working directory
print(os.getcwd())

# List files and folders in current working directory
print(os.listdir())

# List files and folders in another directory
print(os.listdir("C:\\MyDrive\\SelfStudyCode\\Python\\PythonLearning"))

# Move file, copy file
shutil.copy("C:\\MyDrive\\SelfStudyCode\\Python\\PythonLearning\\Basics\\my_test_file.txt", "C:\\MyDrive\\SelfStudyCode\\Python\\PythonLearning")
