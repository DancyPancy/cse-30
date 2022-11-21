def insertionSort(items):
    count = 0
    for i in range(1,len(items)):
        m = items[ i]
        while i > 0 and items[ i-1] > m:
            count += 1
            items[ i] = items[ i-1]
            i -= 1
        print(items[i], m)
        items[ i] = m
    print(count)

list_ = [54,26,93,17,77,31,44,55,20]
insertionSort(list_)
print(list_)