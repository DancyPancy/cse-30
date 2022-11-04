# Function to create combinations
def all_combs(list_, n):
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(list_)):
        m = list_[ i]
        r = list_[i+1:]
        
        for p in all_combs(r, n-1):
            l.append([ m] + p)            
    return l

# Driver code
if __name__=="__main__":
    items ="abcd"
    print(all_combs([x for x in items], 3))