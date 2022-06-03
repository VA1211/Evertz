# colours = {"Red","Orange","Green","Purple","Red"}
# # print(colours)                      #doesnt print duplicate values
# # print(colours[0])                    #not allowed, as set is unordered
# # colours[0] = "Yellow"                # not allowed as set is unchangeble
#
# #accessing set elements:
# for i in colours:
#     print(i)
#
# print("Red"in colours)
#
# #set Methods:
# print(len(colours))
# colours.add("Yellow")               #to add new element
# print(colours)
# set1 = {"a","b","c"}
# set2 = {"d","e","f"}
# set1.update(set2)                   #add elements of other set into one,excludes duplicate
# print(set1)
# set3 = set1.union(set2)             #union creates new set after adding two sets,excludes duplicate
# print(set3)
# list1 = ["g","h"]
# set1.update(list1)                 # we can add tuple,list and set also
# print(set1)
# set1.remove("a")                   #if element is not present,remove will raise an error
# set1.discard("a")                  #if element is not present,remove will not raise an error
# print(set1.pop())                  #set is unordered so we dont know which element will be removed
# set1.clear()                       #empty set is availble
# print(set1)
# del set2                           #deletes full set
# print(set2)
#

name1 = {"a","b","c","d"}
name2 = {"b","c","d"}
# common = name1.intersection(name2)       #creates new set of common elements
# print(common)
# name1.intersection_update(name2)         #changes in existing set
# print(name1)
different = name1.symmetric_difference(name2)
print(different)
name1.symmetric_difference_update(name2)
print(name1)

