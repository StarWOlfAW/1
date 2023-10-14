from collections import Counter
from ex1 import thv

things = thv(input())
que = Counter(things)

print("Элемент | Частота")
print(*[f"{x} | {que[x]}" for x in que], sep="\n")
