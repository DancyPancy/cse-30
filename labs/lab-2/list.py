def list_comprehension(list):
    return [list[i] + list[i+1] for i in range(len(list)-1)]