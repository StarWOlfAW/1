x = input()
y = y1 = int(input())

for i in x:
    if i.isdigit():
        y -= 1
    if y == 0:
        print(f"{y1} цифра в строке : {i}")
