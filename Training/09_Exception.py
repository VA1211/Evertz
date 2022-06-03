#An exception is an event, which occurs during the execution of a program that disrupts the
# normal flow of the program's instructions.

#list1 = [12,45,'d',0]

# for i in list1:
#     try:
#         div = i/3                         #code which can throw exception
#         print(div)
#
#     except:
#         print('wrong input in list')      #code which run if exception occured
#
#     else:
#         print('code in try ran successfully') #code which run if exception is not there

# #sys module is used to know type of exception
# import sys
#
# try:
#     a = 12
#     result = 12/0
#
# except :
#     print(sys.exc_info(),'occured')      #shows which exception occured
#
# finally:
#     print('This code will run anyhow')

#Handling Multiple Esceptions

# try :
#     file = open('text1.txt','r')
#     data = file.read()
#     print(data)
#     number = int(data)
#     result = number/0
#
# except (IOError,ZeroDivisionError):          #multiple exception can be handled
#     print('Error occured')
#
# finally:
#     file.close()

#Raising Exceptions
# try:
#     age = int(input('Enter your age'))
#
#     if age<18:
#         raise ValueError
#     else:
#         print('you are eligible for voting')
#
# except ValueError:
#     print('You are not eligible')

#Assertion
def avg(marks):
    assert len(marks)!=0,'list is empty'     #validation point, runs normally if true otherwise throws exception
    average = sum(marks)//len(marks)
    print(average)

mark = [23,10,24,2]
avg(mark)
mark2 = []
avg(mark2)

