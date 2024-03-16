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
    def __add__(self, other):
        if self.denom != other.denom:
            lcm = (self.denom * other.denom // gcd(self.denom, other.denom))
            first = lcm // self.denom
            second = lcm // other.denom
            yeet = self.numer * first
            wield = other.numer * second
        else:
            yeet = self.numer
            wield = other.numer
            lcm = self.denom
        return Fraction(yeet + wield, lcm)
    def __sub__(self, other):
        if self.denom != other.denom:
            lcm = (self.denom * other.denom // gcd(self.denom, other.denom))
            first = lcm // self.denom
            second = lcm // other.denom
            yeet = self.numer * first
            wield = other.numer * second
        else:
            yeet = self.numer
            wield = other.numer
            lcm = self.denom
        return Fraction(yeet - wield, lcm)
    def __eq__(self, other):
        x = self
        y = other
        x.reduce()
        y.reduce()
        if x.numer != y.numer or x.denom != y.denom:
            return False
        else:
            return True
        


class ReduceFraction(Fraction):
    def __init__(self, numer, denom):
        super().__init__(numer, denom)
        self.reduce()
            
        

##m1 = Fraction(3, 3)
##m2 = Fraction(1, 2)
##print(m1 - m2)


