#Polymorphism - polymorphism means the same function name (but different signatures)
                #    being used for different types.
#inbuilt polymorphic functions
# print(len("MYname"))              #len function for string
# print(len([12,24,34]))            #len function for list

#polymorphism in user-defined function
# def sum(x,y,z=0):          #The ‘self’ variable is used only when working with classes. Be it class
#                          # method or instance variable.
#  return x+y+z
#
# result = sum(12,23)
# print(result)
# print(sum(12,23,56))
#
# #polymorphism with class methods
# class Parrot :
#     def name(self):
#         print('I am parrot')
#     def colour(self):
#         print('My colour is green')
#
# class Crow:
#     def name(self):
#         print('I am crow')
#     def colour(self):
#         print('My colour is black')
#
# mithu = Parrot()
# kalu = Crow()
#
# for bird in (mithu,kalu):
#     bird.name()
#     bird.colour()

#method overriding
#here, inheraitance is must, child class overrides parent class method, means same method name
# but different content
# class Animal :
#     def leg(self):
#         print('I have four legs')
#
#     def colour(self):
#         print('Every animal has different colour')
#
# class Dog(Animal):
#     def identity(self):
#         print('I am dog')
#
#     def colour(self):
#         print('My colour is brown ')
#
# obj_animal = Animal()
# shera = Dog()
# shera.colour()

#method overloading is not allowed directly in python. To achieve this ,multiple dispatch package can be used
# from multipledispatch import dispatch
# class practice:
#     @dispatch(int,int)
#     def sum(self,a,b):
#         return a+b
#     @dispatch(int,int,int)
#     def sum(self,a,b,c):
#         return a+b+c
# obj = practice()
# result = obj.sum(3,6)
# print(result)
#
# result2 = obj.sum(2,5,8)
# print(result2)
#
#Encapsulation
#used to restrict access to methods and variables.
#code and data are wrapped together within a single unit from being modified by accident.

class computer:
    def __init__(self):
        self.__maxprice = 100                 #created private variable by '_'

#getters and setters are used to change private variable
    def getprice(self):
        print(f'selling price us {self.__maxprice}')

    def setprice(self,price):
        self.__maxprice=price

obj = computer()
obj.getprice()
obj.__maxprice = 150                       #will not change value
obj.getprice()
obj.setprice(300)                          #will change value
obj.getprice()

#Abstraction
# used to hide the internal functionality of the function from the users.
# The users only interact with the basic implementation of the function, but inner working is hidden.
# User is familiar with that "what function does" but they don't know "how it does."

#Abstract class - if class has one or more abstract methods, it is called abstract class
#abc module is used for abstraction

from abc import ABC            #ABC=Abstract Base Class
class shapes:
    def sides(self):
        pass

class circle:
    def sides(self):
        print('I have no side')

class square:
    def sides(self):
        print('I have 4 sides')

class traingle:
    def sides(self):
        print('I have 3 sides')

crl = circle()
crl.sides()
sqr = square()
sqr.sides()
trl = traingle()
trl.sides()


