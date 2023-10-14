def num(n: int) -> list:
    y = [0, 1]    #Числа Фиббоначи начинаются с 0
    for _ in range(n - 2):
         y.append(y[-2] + y[-1])
    return y[:n]
    

print(*num(int(input())), sep=", ")
