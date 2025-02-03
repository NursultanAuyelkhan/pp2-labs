#1.
print("Task 1.")

def my_func(grams):
    return 28.3495231 * grams

grams = float(input())
print(my_func(grams))

#2.
print("Task 2.")

def temperature(F):
    return (F - 32) * (5/9)

F = int(input())
print(temperature(F))

#3.
print("Task 3.")
numheads = 35
numlegs = 94


#4.
print("Task 4.")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x - 1):
        if x%i==0:
            return False
    return True
PrimeList = []
def filter_prime():
    for x in nums:
        if isPrime(x):
            PrimeList.append(x)
filter_prime()
print(PrimeList)

#Task 5.
print("Task 5.")
from itertools import permutations
word = input()
def my_func(word):
    p = permutations(word)
    for i in p:
        print(i)
my_func(word)

#Task 6.
print("Task 6.")

string = tuple(input())

def str(n):
    for x in n:
        i = 1
        print(x[len(n) - i])
        i += 1
        i <= len(n)

str(string)
    
