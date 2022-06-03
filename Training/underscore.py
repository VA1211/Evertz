# _ = 3   #variable
# print(_)
#
# numbers = [1,2,3,5,7]
# for _ in numbers:              #temp variable
#     print(_,end=' ')
#
# person = 'vidhi',23,'pune',23000               #packing
# name,_,_,salary = person                       #unpacking
# print(name)
# print(_)

#single leading underscore :
class A:
    def __init__(self):
        self.x = 3
        self._y = 4
        self.__z = 6

# obj = A()
# print(obj.x)
# print(obj._y)
# #print(obj.__z)
# print(obj._A__z)
# print(A.__dict__)
# #single trailing underscore
# #used in names like class_, def_ to use keywords and avoid naming conflicts

import json

mydict = {}

d2 = {}

def dictForm():
    list = []
    for line in file:

        # if : in line then only print or go ahead
        if ':' in line:
            (key, value) = line.strip().split(":", 1)
            mydict[key.strip()] = value.strip()
        else:

            break
with open("original.txt") as file:
    file.readline()
    dictForm()

mydict1 = {}
with open("original.txt") as file1:
    a2 = file1.seek(957)
    # print(a2)

    for line in file1:

        # if : in line then only print or go ahead
        if ':' in line:

            (key, value) = line.strip().split(":", 1)
            mydict1[key.strip()] = value.strip()
        else:

            break

mydict2 = {}
az = open("original.txt", "r")
az.seek(2212)

for line in az:

    # if : in line then only print or go ahead
    if ':' in line:

        (key, value) = line.strip().split(":", 1)
        mydict2[key.strip()] = value.strip()
    else:

        break

d2["General"] = mydict
d2["Video"] = mydict1
d2["Other"] = mydict2



with open("vidhi.json", "w") as filez:
    filez.write(json.dumps(d2, indent=1))

print(d2)
