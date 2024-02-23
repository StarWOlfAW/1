class Fraction:
    def __init__(self, numer=1, denom=1):
        self.numer = numer
        self.denum = denom
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    def input(self):
        self.numer = int(input())
        self.denom = int(input())
        if self.denom == 0:
            return " не делить на ноль!"
##m1 = Fraction()
##m1.input()
##print(m1)



