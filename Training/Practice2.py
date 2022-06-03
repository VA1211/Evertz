class Employee:

    __comapany = "google"

    def __init__(self,salary,name):
        self.__salary = salary
        self.__name = name

Vidhi = Employee(13000,"Vidhi")
print(Vidhi.__dict__)
print(Vidhi._Employee__salary)

print()
