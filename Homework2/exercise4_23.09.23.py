x = input()
l = x.count('(')
r = x.count (')')
if l > r:
    print(f"Не хватает {l - r} закрывающих скобок")
elif r > l:
    print(f"Не хватает {r - l} открывающих скобок")
else:
    print("Все правильно")