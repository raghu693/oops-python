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

Employee.add( 12, 12)
Employee.substract( 12, 13)
Employee.multiply( 12, 12)