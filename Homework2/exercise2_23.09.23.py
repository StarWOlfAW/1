x = input()
y = []
while x:
    y.append(x)
    x = input()
y.sort(reverse=True)
print(''.join(y))
