#python tuples
print(" Python Tuples ")

mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Access Tuple Item
print(" Access Tuple Item")

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Update Tuples
print(" Update Tuples ")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
thistuple = ("apple", "banana", "cherry")

y = list(thistuple)

y.append("orange")
thistuple = tuple(y)

print(y, thistuple)

thistuple = ("apple", "android", "microsoft")
y = ("linux",)
thistuple += y
print(thistuple)

#Unpack Tuples
print(" Unpack Tuples ")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Loop Tuples
print("Loop Tuples")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
for i in range(len(thistuple)):
    print(thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

#Join Tuples
print(" Join Tuples")

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

mytuple = tuple1 * 2
print(mytuple)