# # fruits = ("mango","apple","kiwi","banana","orange")
# # print(fruits)
# #
# # #if only one value is there in tuple ',' is needed
# # colour = ("Red")      #wrong, this is a string
# # print(type(colour))
# # shape = ("circle",)   #correct way
# # print(type(shape))
# #
# # #can use tuple constructor to create tuple
# # name = tuple(("vidhi","shah"))
# # print(name)
# #
# # #slicing operations are same as list
# # print(name[-1])
# #
# # #to check if element is present in tuple
# # if "vidhi" in name:
# #     print("I am present")
# #
# # #tuples are immutable, if want to change something in tuple, have to convert in list and after
# # # operations again convert to tuple
# #
# names = ("rima","tina","shiya","madhuri","naiya")
# print(names)
# list1= list(names)
# print(list1)
# list1.append("shanaya")
# print(list1)
# names = tuple(list1)
# print(names)

#two tuples can be added with + operator
# tuple1 = ("a","b","c")
# tuple2 = ("d","e","f")
# newtuple = tuple1+tuple2
# print(newtuple)

#unpacking tuple
# numbers = ("one","two","three","four","five")
# (a,d,*e)= numbers                      #assigns list to e as variables are less
# print(a)
# print(e)

#iterating in tuple same as list
# names = ("vidhi","rihan","ankin")
# print(*names,sep="\n")
#
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i],end=" ")
#   i = i + 1

#methos for tuple
tuple = ("my","name","is","vidhi","name")
print(tuple.count("name"))
print(tuple.__len__())
print(tuple.index("is"))

