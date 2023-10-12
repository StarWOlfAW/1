from ex1 import thv

def mid(*num) -> float:   #каждое число  к float
    return sum(num) / len(num)

print(mid(*map(int, thv(input()))))
# map выступает вместо for 
# Instead of using a for loop, the map() function provides a way of applying a function to every item in an iterable.
# Тоесть вместо счета количества элементов в списке и for можно взять map(??) ну вроде работает
