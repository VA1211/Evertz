
# class car:
#     '''This is a docstring'''
#     engine = 'petrol'                   #class attribute, same for all objects
#
#     def __init__(self,colour,wheels):     #constructor , initialises variables
#         self.colour = colour
#         self.wheels = wheels
#
#     @staticmethod
#     def music():                        #if method is static, self parameter is not required nd can be
#                                         # called without creating object
#         return 'I have music system'
#
#     def greet(self):
#         print(f'my colour is {self.colour}')
#
# print(car.music())
# #car.greet()                             #not allowed as not static method,need object
# print(car.__doc__)                      #returns docstring

#Hyundai = car()                         #created object
# print(Hyundai.music())                  #static method calling with object
# print(Hyundai.greet())

# Tata = car("red","4")                            #calls constructor
# result = Tata.greet()                    #equals to Car.greet(Tata) , object is passed as parameter

#
# print(Tata.colour)                           #accesseing instance variables
# print(Tata.engine)                           #accessing class variable through object

#complex number

# class complexnumber:
#
#     def __init__(self,r,i):
#         self.real = r
#         self.imagine = i
#
#     def get_value(self):
#         print(f'{self.real}+{self.imagine}i')
#
#     def sum(self,a,b):
#         sum_real = a.real + b.real
#         sum_imagine = a.imagine + b.imagine
#         print(f'Sum is : {sum_real}+{sum_imagine}i')
#
# number1 = complexnumber(2,43)
# number2 = complexnumber(3,23)
# sum = complexnumber(0,0)
#
# number1.get_value()
# number2.get_value()
#
# sum.sum(number1,number2)

#inheritance
#Single level
# class A:                                  #parent class
#     name = 'A'
#     def greet(self):
#         print('I am method of A')
#
# class B(A):                              #child class inharitates parent class
#     def name(self):
#         print('I am method of B')
#
#
# Rishi = B()                             #child class's object can access methods of parent class as well
# Rishi.greet()
# Rishi.name()
#
# Mina = A()                               #parent class object can access only parent class methods
# Mina.greet()

#Multilevel inheritance
class GrandFather:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def identity(self):
        print("I am grandfather's method")

class father:
    def __init__(self,salary,name,surname):
        self.salary = salary
        GrandFather.__init__(self,name,surname)

    def greet(self):
        print('Hello... !!')

class son:
    def __init__(self,id,salary,name,surname):
        self.id = id
        father.__init__(self,salary,name,surname)
    def getname(self):
        print("My name is son")


Adi = son(12,12000,'Adi','shah')
print(Adi.id)
print(Adi.salary)


