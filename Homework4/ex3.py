def afe(y) ->bool:
    return len(y) == len(set(y))


if __name__ == "__main__":
    print(afe(input().split()))