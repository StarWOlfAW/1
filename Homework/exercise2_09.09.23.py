a = float(input("Введите A"))
b = float(input("Введите B"))
c = float(input("Введите C"))
d = float(input("Введите D"))
f = float(input("Введите F"))
y = f - d
if  y == 0:
    print("Делить на ноль нельзя")
else: 
    x = ((a * b - c) / (f - d))
    print(x)