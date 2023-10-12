def thv(x) -> list:

    que = []
    while x:
        que.append(x)
        x = input()
    return que


print(thv(input()))
