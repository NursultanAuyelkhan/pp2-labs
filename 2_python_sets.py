#python sets
myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry", "apple", True, 1, 2}
print(thisset)
print(len(thisset))

print(type(myset))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

#Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)

#Add Set Items
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

#Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)

thisset.discard("apple")

print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2 ,3}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)

print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)