from collections import deque


def search(gr, st, cur):
    if not gr:
        return None
    k = deque([(st, 0)])
    d = set([st])
    while k:
        this, forward = k.popleft()
        if this == cur:
            return forward
        for near in gr.get(this, []):
            if near not in d:
                k.append((near, forward + 1))
                d.add(near)

    return None
