class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summation(self):
        return self.a + self.b

    def substraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


obj1 = Calculator(10, 5)
print(obj1.summation())
print(obj1.substraction())
print(obj1.multiplication())
print(obj1.division())
