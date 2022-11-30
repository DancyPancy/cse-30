# make a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:] 

def nqueen(n):
    solutions = []
    for i in all_perms([i+1 for i in range(n)]):
        solution = True
        for j in range(n):
            xpos = j
            ypos = i[j]
            for k in range(n):
                if j != k:
                    if (xpos - k)**2 == (ypos - i[k])**2:
                        solution = False
                        break
        if solution:
            solutions.append(i)

    return solutions

if __name__ == '__main__':
    while True:
        try:
            n = int(input('Enter a number of queens:\n'))
            break
        except:
            print('That\'s not a number!')

    solutions = nqueen(n)
    print(f'The {n}-queens puzzle has {len(solutions)} solutions:')
    for i in solutions:
        print(i)

    