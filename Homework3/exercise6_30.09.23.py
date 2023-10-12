def numby(num, cur = 1, c = 0):
    for i in range (num):
        if num % cur == 0:
            c += 1
            cur += 1
        elif num % cur != 0:
            cur += 1
            continue
    if c > 2:
        return False
    else:
        return True
    
print(numby(int(input())))