def triangles():
    l = [1]
    yield l
    while(1):
        l = [1] + [l[i] + l[i+1] for i in range(len(l) - 1)] + [1]
        yield l
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
