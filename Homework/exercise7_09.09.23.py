from math import ceil, floor

x = ceil(float(input("Введите X")))
y = floor(float(input("Введите Y")))
n = 0
for z in range (x, y + 1):
    if z % 5 == 0 :
      n = n + z
print(n)