from math import gcd
class Fraction:
    def __init__(self, numer = 1, denom = 1):
        self.numer = numer
        self.denom = denom
        if self.denom == 0:
            raise ZeroDivisionError("Деление на ноль")
    def __str__(self):
        if self.denom == 0:
            return "Деление на ноль"
        else:
            return str(self.numer) + "/" + str(self.denom)
    def input(self):
        self.numer = int(input())
        self.denom = int(input())
        if self.denom == 0:
            return "Деление на ноль"
    def reduce(self):
        print(gcd(self.numer, self.denom))
        self.numer /= gcd(self.denom, self.numer)
        self.denom /= gcd(self.denom, self.numer)
            
        


m1 = Fraction(11, 22)
m1.reduce




