import re
#Task 1.
print("Task 1.")


x = input()

if re.fullmatch(r'^ab*$', x):
    print("Match found!")
else:
    print("Match not founded!")

#Task 2.
print("Task 2.")


x = input()

if re.fullmatch(r'ab{2,3}', x):
    print("Match founded!")
else:
    print("Not founded!")

#Task 3.
print("Task 3.")

x = input()

if re.findall(r'[a-z]+_[a-z]+', x):
    print("True")
else:
    print("False")

#Task 4.
print("Task 4.")

x = input()
if re.findall(r'^[A-Z][a-z]+', x):
    print("Founded")
else:
    print("Not founded")

#Task 5.
print("Task 5.")

x = input()

if re.findall(r'a.*b', x):
    print("True")
else:
    print("False")

#Task 6.
print("Task 6.")

txt = input()

x = re.sub("[\s,\.]", ":",txt)
print(x)

#Task 7.
print("Task 7.")

txt = input()

x = re.sub(r'_(\w)', lambda match: match.group(1).upper() , txt)

print(x)

#Task 8.
print("Task 8.")

txt = input()

x = re.split("[A-Z]", txt)

print(x)

#Task 9.
print("Task 9.")
text = input()

x = re.sub(r'([A-Z])', r' \1', text).strip()

print(x)

#Task 10.
print("Task 10.")
camel = input()

x = re.sub(r'([A-Z])', r'_\1', camel).lower()
print(x)