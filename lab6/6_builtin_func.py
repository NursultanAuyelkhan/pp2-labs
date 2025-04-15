#Task 1.
print("Task 1.")

size_list = input()
my_list = list(map(int, size_list.split()))
multiply = 1

for i in my_list:
    multiply *= i

print(multiply)

#Task 2.
print("Task 2.")

def count():
    upper = 0
    lower = 0
    string = input()
    for i in string:
        if i >= "A" and i<="Z":
            upper+=1
        else:
            lower+=1
    
    print(upper)
    print(lower)
count()

#Task 3.
print("Task 3.")

def palindrome():
    string1 = input()
    string2 = string1[::-1]
    if string1 == string2:
        print("Palindrome")
    else:
        print("Isn't palindrome")

palindrome()

#Task 4.
print("Task 4.")

import math
import time

time_miliseconds = int(input())
time2_miliseconds = int(input())

print(f"Square root of {time_miliseconds} after {time2_miliseconds} miliseconds is {math.sqrt(time_miliseconds)}")

#Task 5.
print("Task 5.")

def check_all():
    tpl = input()
    values = tuple(map(int, tpl.split()))

    print(all(values))
check_all()