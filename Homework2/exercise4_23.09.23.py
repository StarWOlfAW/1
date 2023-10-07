x = input()
y = x.count('(')
r = x.count(')')
if y > r:
    print(f"Не хватает {y - r} закрывающих скобок")
elif r > y:
    print(f"Не хватает {r - y} открывающих скобок")
else:
    print("Все правильно")
