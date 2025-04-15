#Task 1.
print("Task 1.")
import os

path= r"/Users/nurik/Desktop/labs"
all= list(os.listdir(path))
print(all)

#Task 2.
print("Task 2.")
file_path = "lab6.txt"
if os.path.exists(file_path):
    print("This file exists!")
    f = open(file_path, "r")
    print(f.read())
else:
    print("This file doesn't exist!")

f = open(file_path, "w")
f.write(input())

f = open(file_path, "r")
print(f.read())

if os.access(file_path, os.X_OK):
    print("File is executable!")
else:
    print("File isn't executable!")

#Task 3.
print("Task 3.")

file = r"/users/Nurik/Desktop/labs/lab6.txt"

if os.path.exists(file):
    print("Exist!")
    print(os.path.basename(file))
    print(os.path.dirname(file))
else:
    print("Doesn't exist!")

#Task 4.
print("Task 4.")

file = "lab6.txt"
f = open(file, "r")
lines = sum(1 for lines in f)
print(lines)

#Task 5.
print("Task 5.")

file = "lab6.txt"
my_list = {"aitu", "iitu", "nu", "kaznu"}
with open(file, "w") as f:
    for item in my_list:
        f.write(item + "\n")
with open(file, "r") as f:
    print(f.read())

#Task 6.
print("Task 6.")

import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, "w") as file:
            file.write("hello world")

if __name__ == "__main__":
    generate_files()

#Task 7.
print("Task 7.")

def copy_file():
    string = input("File name:")
    with open(string, "r") as file:
        data = file.read()
    
    if '.' in string:
        copy_path = string.replace('.', '_1.', 1)
    
    with open(copy_path, "w") as file_copy:
        file_copy.write(data)

copy_file()

#Task 8.
print("Task 8.")

def delete():
    file_name = input()
    if os.path.exists(file_name):
        print("Exists.")
        if os.access(file_name, os.W_OK):
            os.remove(file_name)
            print("Deleted.")
        else:
            print("No write")
    else:
        print("Doesn't exist.")

delete()
