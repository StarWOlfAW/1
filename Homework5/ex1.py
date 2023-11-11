def find_bin(place, num):
    small = 0
    big = len(place) - 1
    this = None
    while small <= big:
        mid = (small + big) // 2
        if place[mid] >= num:
            this = mid
            big = mid - 1
        else:
            small = mid + 1
    return this
