from Homework3.ex1 import thv


def swap(pl: list, k: int) -> list:
    k %= len(pl)
    return pl[-k:] + pl[:-k]


if __name__ == "__main__":
    print(swap(thv(input()), int(input())))
