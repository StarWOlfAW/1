def thv(x) -> list:

    que = []
    while x:
        que.append(x)
        x = input()
    return que
if __name__ == "__main__":
    print(thv(input()))
