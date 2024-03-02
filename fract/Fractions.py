from math import gcd
class Fraction:
    def __init__(self, numer = 1, denom = 1):
        self.numer = numer
        self.denom = denom
        self.validate()
        
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    
    def input(self):
        try:
            self.numer = int(input())
            self.denom = int(input())
            self.validate()
        except ValueError:
            print ("Вводите только десятеричные числа")
            return False
        return True

    def reduce(self):
        greatcd = gcd(self.numer, self.denom)
        self.numer = self.numer // greatcd
        self.denom = self.denom // greatcd

    def validate(self):
        if self.denom == 0:
            raise ZeroDivisionError("Деление на ноль")


class ReduceFraction(Fraction):
    def __init__(self, numer, denom):
        super().__init__(numer, denom)
        self.reduce()
            
        


##m1 = Fraction(-10, -20)
##m1.input()



