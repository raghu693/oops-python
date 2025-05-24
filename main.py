class Employee:
    def __init__(self, name):
        self.__name = name
        print("Constructor Running, Right Now");

    def add(a, b):
        sum = a + b
        print(sum)

    def substract(a, b):
        difference = a-b
        print(difference)

    def multiply(a, b):
        product = a*b
        print(product)

    def division(a, b):
        division = a/b
        print(division)

    def floor_division(a, b):
        floorDivision = a//b
        print(floorDivision)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

Employee.add( 12, 12)
Employee.substract( 12, 13)
Employee.multiply( 12, 12)
Employee.division( 26, 12)
Employee.floor_division( 25, 12)

E1 = Employee("Raghav")
print(E1.get_name())
E1.set_name("Ayush")
print(E1.get_name())