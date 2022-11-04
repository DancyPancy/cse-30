def sum_list(num):
    if len(num) == 0:
        return None
    elif len(num) == 1:
        return num[0]
    else:
        return num[0] + sum_list(num[1:])

if __name__ == "__main__":
    listA = []
    listB = [3]
    listC = [1, 2, 3, 4]
    assert sum_list(listA) == None
    assert sum_list(listB) == 3
    assert sum_list(listC) == 10
    print('Everything works correctly!') 