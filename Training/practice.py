# import json
# with open("C:\\Users\\vidhi.shah\\Desktop\\Evertz\\Sample files\\EmployeeData.json") as file:
#     data = json.load(file)
#     print(data)
#     print(type(data))
#     print(data[0]['id'])
#
# if(data[0]['name']=='manoj'):
#     assert data[0]['id']==4051
#     print("the result is correct")

# data = {'name':'vidhi','surname':'shah','company':'yash','id':202}
# with open("myjason.json","w") as newfile:
#     json.dump(data,newfile)

# mystring = {'name':'vidhi','surname':'shah','company':'yash','id':202}
# print(type(mystring))
# j1 = json.dumps(mystring,indent=4,sort_keys=True)
# print(j1)
# print(type(j1))

# import xml.etree.ElementTree as ET
#
# data = ET.parse('employee.xml')
# root = data.getroot()
# print(root)
# print(root.tag)
# print(root.attrib)
#
# # for i in root[0]:
# #     print(i.tag,i.attrib)
#
# # for i in root.iter():
# #     print(i.tag)
#
# for i in root.iter('name'):
#     print(i.attrib)

# str1 = "Twinkle, twinkle, little star, \n  How I wonder what you are! \n\tUp above the world so high,\n\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n  How I wonder what you are"
# print(str1)
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

#my python version
import sys
print("My Python Version : ",sys.version)
print("Version Info :", sys.version_info)

# from datetime import datetime
# mydate = datetime.today().date()
# date = mydate.strftime("%d/%m/%Y")
# print("current date :",date)
# print("current time :", datetime.now().time())

# import math
# def areaOfCircle(r):
#     area = math.pi*r*r
#     return area
#
# radius = float(input("Enter radius of circle : "))
# a = areaOfCircle(radius)
# print("Area of Circle : ",a)

# fname = input("Enter your First name : ")
# lname = input("Enter your Last name : ")
# print(lname+" "+fname)

# numbers = input("Enter numbers with comma : ")
# mylist = numbers.split(",")
# print(mylist)
# mytpl = tuple(mylist)
# print(mytpl)
#converting text file into dictonary

#20/5
# fileName = input('Enter file name with extension')
# words = fileName.split(".")
# print("File Extension is : ",words[-1])

# examDate = (12,5,2025)
# print("Exam Date is : ",examDate[0],"/",examDate[1],"/",examDate[2])
# print("Exam starting at : %i/ %i /%i"%examDate)

# number = int(input('Enter a number : '))
# result = number + (number*10 + number)+(number*100 +number*10 +number)
# print(result)

# import calendar
# print(calendar.calendar(2022))

# from datetime import date
# date1 = date(2022,4,30)
# date2 = date(2021,3,20)
# difference = date1 -date2
# print(difference)

# number = int(input("Enter a number : "))
# def difference(number):
#     if number>17:
#         return number-17
#     else:
#         return (17-number)*2
#
# print(difference(number))
# import json
# mydict = {}
# with open("C:\\Users\\vidhi.shah\\Downloads\\original.txt") as file:
#     for line in file:
#         if ':'in line:
#             (key,value) = line.strip().split(":",1)
#             mydict[key.strip()] = value.strip()
# print(mydict)
# print(type(mydict))
# with open("mynewjson.json","w") as file2:
#   file2.write(json.dumps(mydict,indent=4))
#
# def sum(a,b,c):
#     if(a==b and a==c):
#         return 3*(a+b+c)
#
#     else:
#         return a+b+c
#
# num1 = int(input("Enter first num : "))
# num2 = int(input("Enter second num : "))
# num3 = int(input("Enter third num : "))
# sum = sum(num1,num2,num3)
# print("result is : ",sum)

# Str = "this you?"
# def strManipulation(line):
#     if Str[:2]=="Is":
#         return Str
#     else:
#         return "Is "+ Str
#
# print(strManipulation(Str))

# num = int(input("How many times you want copy of string?"))
# word = "Strong"
# result = num * word
# print(result)

# list = [12,23,23,4,2,4,6,4,7,4]
# count = 0
# for i in list:
#     if i==12:
#         count+=1
#
# print(count)
#
# word = "Honest"
# ln = len(word)
# n =4
# if ln>=2:
#     print(n*word[:2])
#
# else:
#     print(n*word)
#
# letter = input("Enter A LETTER : ")
# if(letter=='a'or letter =='i'or letter=='e'or letter=='o'or letter=='u'):
#     print("This is vowel")
#
# else:
#     print("This is consonent")

# list = [12,34,65,78,23]
# if 34 in list:
#     print("True")
# else:
#     print("False")

# lst = [2,4,7,3]
#
# def histograf(list):
#     for i in list:
#         op = (i*'@')
#         print(op)
#
# histograf(lst)

# list = ["My","Name","Is","Vidhi"]
# str = ""
# for i in list:
#     str = str + i + " "
# print(str)

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# lst = []
# for i in numbers:
#     if i>=237 and i%2==0:
#         lst.append(i)
# print(lst)

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1-color_list_2)
# print(color_list_1.difference(color_list_2))
#
# lst1 = [12,34,56,37]
# lst2 = [13,25,12]
# print(set(lst1)-set(lst2))
#
# print(lst1+lst2)
# for i in lst1+lst2:
#     if (i not in lst1) or (i not in lst2):
#         print(i)

# a = 12
# b = 12.45
# if type(a)==int and type(b)==int:
#     print(a+b)
# else:
#     print("WRONG INPUT")

# a = 12
# b = 13
# if isinstance(a,int) and isinstance(b,int):
#     print(a+b)
# else:
#     print("OBJECT IS NOT INTEGER")
#
# import os
# print("MyFile path is :", os.path.realpath(__file__))

# str1 = "1234566"
# myint = int(str1)
# print(myint)
# type(myint)
# myfloat = float(str1)
# print(myfloat)
# type(myfloat)
#
# n = int(input("Enter  a number : "))
# sum=0
# for i in range(n+1):
#     sum = sum + i
# print(sum)

# num = int(input("enter a 4 digit no : "))
#
# sum = 0
# while num>0:
#     temp = num % 10
#     sum = sum + temp
#     num = num//10
# print(sum)

# a = 12
# b = 24
# c = 16
# min = min(a,b,c)
# max = max(a,b,c)
# mid = (a+b+c)-min -max
# print("Sorted : ",min,mid,max)

#print(copyright())

# help('xml.dom')
#
# lst1 = ['circle','rectangle','square']
# str = ' '
# str = str.join(lst1)
# print(str)
#
# str1 = ''
# for i in lst1:
#     str1 = str1+' '+i
# print(str1)

# lst1 = [1,3,7,5]
# # print(sum(lst1))
#
# sum = 0
# for i in lst1:
#     sum = sum + i
# print(sum)

# dict = {'a':20,'b':30,'c':60}
# sum = 0
# for i in dict:
# 	sum = sum + dict[i]
# print(sum)

# list = [12,34,11,5,7,3,56]
# num = 6
# for i in list:
# 	if i>num:
# 	    print(f'{i} is greater than {num}')
# 	else:
# 		print(f'{i} is less than {num}')

# str = 'I am a girl. I like to go to office.'
# mystr = str.upper()
# print(mystr.count('I'))
#
# string1 = 'vidhi shah'
# print("Length of string is : ",len(string1))
# count = 0
# for char in string1:
# 	count = count + 1
# print("Length of string is : ",count)
#
# print(string1[0].upper()+string1[1:])
#
# dict = {}
# for char in string1:
# 	keys = dict.keys()
# 	if(char in keys):
# 		dict[char]+=1
# 	else:
# 		dict[char]= 1
# print (dict)

# def newString(str):
#     if len(str)>=2:
#         new = str[:2]+str[-2:]
#         print(new)
#     else:
#         new = ''
#         print("String is Empty")
# newString('Y')
#
# def changedString(str):
#     for char in str:
#         if str[0]==char:
#             new = str[0]+ str[1:].replace(char,'$')
#             return new
#
# print(changedString("restart"))

# str1 = "abc"
# str2 = 'xyz'
# new = str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
# print(new)

# String = 'Ya'
# length = len(String)
# if length>=3 :
# 	if String[-3 :] != 'ing':
# 		new = String + 'ing'
# 		print(new)
# 	else :
# 		new =String[:-3]+'ly'
# 		print(new)
# else:
#     new = String
#     print(new)

# String = 'The lyrics is not that poor! The lyrics is poor!'
# a = String.index('not')
# print(a)
# b = String.find('poor')
# print(b)
# if b>a:
#     str = String.replace(String[a:b+4],'good')
#     print(str)
# else:
#     str = String
#     print(str)

# list = []
# for i in range(5):
#     a = input("Enter a word in list")
#     list.append(a)
# print("Entered list is : ",list)
#
# max = ''
# for word in list:
#     if len(word)>len(max):
#         max = word
#
# print("Longest word is : ",max)

# def removeIndex(str,n):
#     first = str[:n]
#     second = str[n+1:]
#     newStr = first +second
#     print(newStr)
#
# removeIndex("India is the best",3)
#

# str = 'Welcome office!! '
# for i in range(0,len(str)):
#     if i%2==0:
#         print(str[i],end='')


