from ex1 import thv

things = thv(input())
que = {}

for th in things:
    que[th] = que.get(th, 0) + 1

print("Элемент | Частота")
print(*[f"{x} | {que[x]}" for x in que], sep = "\n")