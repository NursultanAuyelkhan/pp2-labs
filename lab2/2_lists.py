#python lists
thislist = ["apple", "banana", "cherry"]
print(thislist)

list1 = ["abc", "34", True, 40, "male"]
print(type(list1))

list = ["apple", "banana", "cherry"]
print(type(list))

#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print(thislist[-1])

thislist = [1,2,3,4,5,6,7,8,9,10]

print(thislist[3:7])
print(thislist[:2])
print(thislist[3:])

list2 = ["car", "bike", "plane"]

if "bike" in list2:
    print("Yes, 'bike' is in list2")

#Change List Items

thislist = [1,2,3,4,5]
thislist[2] = "three"
print(thislist)

thislist.insert(3, "watermelon")
print(thislist)

#Add list items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # it adds word to end
print(thislist)

thislist.insert(1,"orange")
print(thislist)

tropical = ["mango", "pineapple"]
thislist.append(tropical)
print(thislist)

#Remove List Items

thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.reverse()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key = str.lower)
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

mylist = thislist[:]
print(mylist)

#Join Lists
list1 = ["a", "b", "c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)