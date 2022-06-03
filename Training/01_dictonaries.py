# mydict = {"new":"something which is not old",23:"a number"}
# print(mydict)
# print(mydict[23])
# print(mydict.keys())              #prints list of keys
# mydict["add"]="updated"              #added new element
# print(mydict)
# print(mydict.values())
# print(mydict.items())
# mydict2 = {"rihan":"part of god vishnu"}
# mydict.update(mydict2)                 #adding two dictionaries
# print(mydict)
# mydict.pop(23)
# print(mydict)
# mydict.popitem()                      #deletes last item of dict
# print(mydict)
# mydict.clear()
# print(mydict)
# del mydict2
# print(mydict2)
#
# #iterating keys and values from dictionary
#

colours = {"vidhi": "pink", "Rihan": "Red", "Ankin": "blue"}
# printing keys
for i in colours:
    print(i,end=" ")

for i in colours.keys():
    print(i)

# printing values
for i in colours:
    print(colours[i])

for i in colours.values():
    print(i)

#printing pairs
for x,y in colours.items():
    print(x," : ",y)

#nested Dictionaries
Students = {"name1" : {
             "id" : 13,
             "school" : "PCN HighSchool"},
            "name2":{
            "id":14,
            "school":"saraswati"
            }}

print(Students)

employee1 = {"id":103,"salary":12456}
employee2 ={"id":106,"salary":128399}

company = {"employee1":employee1,"employee2":employee2}
print(company)