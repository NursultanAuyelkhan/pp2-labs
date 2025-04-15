#Task 1.
print("Task 1.")

class String():
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

MyString = String()
MyString.getString()
MyString.printString()

#Task 2.
print("Task 2.")

class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

a = float(input())
mysquare = Square(a)
print(mysquare.area())

#Task 3.
print("Task 3.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

a = int(input())
b = int(input())

myarea = Rectangle(a, b)
print(myarea.area())

#Task 4.
print("Task 4.")

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x} , {self.y}")
    
    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        distance = math.sqrt(dx **2 + dy **2)
        return distance 

a = float(input())
b = float(input())

point1 = Point(a, b)
point2 = Point(a, b)

point1.show()

k = float(input())
p = float(input())

point1.move(k,p)
point1.show()

distance = point1.dist(point2)
print(distance)

#Task 5.
print("Task 5.")

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}, {self.balance}")
        else:
            print("Deposit must be positive.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money.")
        elif amount > 0:
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print("The withdraw must be positive.")

account = Account("Nursultan", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.deposit(-100)
account.withdraw(200)

#Task 6.
print("Task 6.")

isprime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))

a = int(input())
print(isprime(a))

