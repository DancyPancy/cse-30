
def make_dict(w_list):
    dictionary = {}
    for word in w_list:
        length = len(word) if len(word) < 10 else 10
        try:
            dictionary[length].append(word)
        except KeyError:
            dictionary[length] = [word]
    return dictionary

if __name__ == '__main__':
    
    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print (dictionary)
    assert dictionary == d
    print('Everything works correctly!')