#Task 1.
print("Task 1.")

def square(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1

a = int(input())
for num in square(a):
    print(num)

#Task 2.
print("Task 2.")
number = int(input())

def even(n):
    i = 1
    while i < n:
        if i%2 == 0:
            yield i
        i += 1

for num in even(number):
    print(num)

#Task 3.
print("Task 3.")

def iterate(n):
    i = 1
    while i < n:
        if i%3 == 0 and i%4 == 0:
            yield i
        i += 1

n = int(input())
for num in iterate(n):
    print(num)

#Task 4.
print("Task 4.")

def squares(a, b):
    i = a
    while i <= b:
        yield i **2
        i += 1

a = int(input())
b = int(input())

for num in squares(a, b):
    print(num)

#Task 5.
print("Task 5.")

def down(n):
    i = n
    while i > 0:
        yield i
        i -= 1

a = int(input())
for num in down(a):
    print(num)

