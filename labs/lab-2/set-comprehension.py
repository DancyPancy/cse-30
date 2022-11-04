nums = [ x for x in range (10) ]
set1 = {var for var in nums if var % 2 == 0}
print(sorted(set1))

words = ['parent', 'mom', 'dad', 'daughter', 'son']
set2 = { n[::-1] for n in words }  
print(sorted(set2))