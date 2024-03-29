# using a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:] 

if __name__ == '__main__':
    data = [1,2,3,4]
    count = 0
    for i in all_perms(data):
        print(i)
        count += 1
    print(count)