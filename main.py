class Employee:
    def __init__(self):
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

Employee.add( 12, 12)
Employee.substract( 12, 13)
Employee.multiply( 12, 12)
Employee.division( 26, 12)
Employee.floor_division( 25, 12)