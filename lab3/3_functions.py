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

def solve(numheads, numlegs):
    for y in range(numheads + 1):
        x = numheads - y
        if 2 * x + 4 * y == numlegs:
            return x, y
    return "No solution"

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print (f"Chickens: {chickens}, Rabbits: {rabbits}")

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
def reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

sentence = input()
print(reverse(sentence))

#Task 7.
print("Task 7.")
 
list1 = [1, 2, 3, 2, 3, 3, 1]
list2 = [3, 2, 3, 4, 5, 1]
list3 = [3, 3, 1, 3, 2, 1]

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33(list1))
print(has_33(list2))
print(has_33(list3))

#Task 8.
print("Task 8.")

list1 = [1, 2, 4, 0, 0, 7, 5]
list2 = [1, 0, 2, 4, 0, 5, 7]
list3 = [1, 7, 2, 0, 4, 5, 0]

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

print(spy_game(list1))
print(spy_game(list2))
print(spy_game(list3))

#Task 9.
print("Task 9.")

n = float(input())

def volume(num):
    return 4/3 * 3.14 * num **3
print(volume(n))

#Task 10.
print("Task 10.")

def unique(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            continue
    print(unique_list)

my_list = [1,4,5,2,1,1,4,6,7,8,10,12]

unique(my_list)

#Task 11.
print("Task 11.")

def is_palindrome(s):
    cleaned_s = ''.join(e.lower() for e in s if e.isalnum())
    return cleaned_s == cleaned_s[::-1]

a = input()
print(is_palindrome(a))

#Task 12.
print("Task 12.")

def histogram(list):
    for i in list:
        print('*' * i)

my_list = [1, 2, 3, 4, 5, 6] 
histogram(my_list)

#Task 13.
print("Task 13.")
import random

random_number = random.randint(1,20)

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")

attempts = 0

while attempts < 6:
    guess = int(input())
    attempts += 1
    if guess < random_number:
        print("Your guess is too low.")
        print("Take a guess.")
    elif guess > random_number:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in 3 guesses!")

if guess != random_number:
    print(f"Sorry, {name}. The number I was thinking of was {random_number}.")     