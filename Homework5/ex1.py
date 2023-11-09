from Homework3.ex1 import thv


def find_bin(place, num):
    mid = len(place) // 2
    small = 0
    big = len(place) -1
    while place[mid] != num and small <= big:
        if num > place[mid]:
            small = mid + 1
        else:
            big = mid - 1
        mid = (small + big) // 2

    if small > big:
        return("NaN")
    else:
        return mid


if __name__ == "__main__":
    print(find_bin(list(map(float, thv(input()))), float(input())))
