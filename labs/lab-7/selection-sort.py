def selectionSort(items):
    count = 0
    for i in range(len(items)-1,0,-1):
        m=0
        for j in range(1,i+1):          # find the maximum in the range
           if items[ j] > items[ m]:
               m = j   
        if i != m:       
            count += 1
            print(count, items[m], items[i])
        items[ m], items[ i] = items[ i], items[ m]

list_ = [54,26,93,17,77,31,44,55,20]
selectionSort(list_)
print(list_) 