a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

x = "Hello"
y = 15
#true
print(bool(x))
print(bool(y))

#false 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True

print(myFunction())

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))


def myFunction() :
    return True

print(myFunction())

x = 200
print(isinstance(x, int))