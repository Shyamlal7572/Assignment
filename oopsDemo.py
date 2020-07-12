class Calculator():
    num=100

    def __init__(self, a, b):
        self.firstname = a
        self.secondname = b

    def Summation(self):
        return self.firstname + self.secondname + self.num

obj = Calculator(2,3)
print(obj.Summation())