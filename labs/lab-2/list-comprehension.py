nums = [ x for x in range (10) ]
print(nums)

squares = [x**2 for x in range(1, 11)]
print(squares)

odd_nums = [ x for x in range (10) if x % 2 == 1 ]
print(odd_nums)

filter_nums = [ 0 if x % 2 == 0 else 1 for x in range (10) ]
print(filter_nums) 