from random import randint

pc = randint(0, 100)
my = int(input())
while pc != my:
    if pc > my:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    my = int(input())
print("Вы угадали число")
