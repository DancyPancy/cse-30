def generator1():
    s = "The first string"
    yield s
    s = "The second string"
    yield s

g1 = generator1()
print(type(g1))

print(next(g1))

print(next(g1))

g1 = generator1()
for k in g1:
        print(k)

def generator2():
    n = 0
    while True:
        yield n
        n += 1

g2 = generator2()
i = 0
while i < 3:
    print(next(g2), end=" ")
    i += 1