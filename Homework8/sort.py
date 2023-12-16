import math

def buble(list):
    for i in range(0, len(list) - 1):
        for k in range(0, len(list) - 1):
            if (list[k] > list[k+1]):
                list[k], list[k+1] = list[k+1], list[k]
    return list


def quick(list):
    if len(list) <= 1:
        return list
    else:
        medium = math.ceil(len(list)/2)
        q = list[medium]
        b = []
        s = []
        m = []
        for n in list:
            if n < q:
                b.append(n)
            elif n > q:
                s.append(n)
            else:
                m.append(n)
        return quick(b) + m + quick(s)


def Stalin(list):
    if len(list) == 0:
        return list
    else :
        sorted = [list[0]]
        for i in range(1, len(list)):
            if list[i] >= sorted[-1]:
                sorted.append(list[i])
        return sorted
    

#if __name__ =='__main__':
    #(listt) = [5, 1, 4, 7, 3, 2, 6]
    #srt = Stalin(listt)
    #print(srt)
    