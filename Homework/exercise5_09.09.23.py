x = float(input("Введите x "))
y = float(input("Введите y "))
if x > 0 and y > 0:
     print("Точка в 1 четверти")
elif x < 0 and y > 0:
     print("Точка в 2 четверти")
elif x < 0 and y < 0: 
     print("Точка в 3 четверти")
elif x > 0 and y < 0:
     print("Точка в 4 четверти")
elif x == 0 and y != 0:
     print("Точка на оси Y")
elif x != 0  and y == 0:
     print("Точка на оси X")
else:
     print("Точка в начале системы кооржинат")