nums = [ x for x in range (10) ]
gen = (x for x in nums if x % 2 == 0)
print(type(gen))

print("Generator sequence:", end = ' ')
for k in gen:
    print(k, end = ' ')

words = ['parent', 'mom', 'dad', 'daughter', 'son']
palindrome_selector = (x for x in words if x == x[::-1])
print("\nPalindromes:", end = ' ')
for k in palindrome_selector:
    print(k, end = ' ')