nums = [ x for x in range (10) ]
cubes = { n : n**3 for n in nums }  
print(cubes)

words = ['parent', 'mom', 'dad', 'daughter', 'son']
d = { n : len(n) for n in words }  
print(d)
