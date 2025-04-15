import math
#Task 1.
print("Task 1.")
from math import radians

num = int(input("Input degree: "))

rad = radians(num)

print(f"Output radian: {rad}")

#Task 2.
print("Task 2.")

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

area = (a+b)/2 * h

print(f"Expected Output: {area}")

#Task 3.
print("Task 3.")
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

area = int((sides * length**2)/(4 * math.tan(math.pi/sides)))


print(f"The area of the polygon is: {area}")

#Task 4.
print("Task 4.")

length = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

area = length * height
print(f"Expected Output: {area}")