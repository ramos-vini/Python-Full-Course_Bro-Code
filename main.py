import os

file_path = "/Users/viniciusramos/Desktop/test.txt"

if os.path.exists(file_path):
    print("The path exists.")
    if os.path.isfile(file_path):
        print("And it is a file.")
    elif os.path.isdir(file_path):
        print("And it is a directory.")
else:
    print("The path does not exist.")
