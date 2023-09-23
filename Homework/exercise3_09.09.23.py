from math import sqrt #Это мне предложил сам VS code. Похоже что это импорт команд из библиотеки?????

x = float(input("x ="))
y = float(input("y ="))
z = float(input("z ="))
v = sqrt(x * x + y * y + z * z) 
print("Длина вектора равна ", v)