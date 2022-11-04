# iterate two items at a time and return a single result (sum, product, etc.)
from functools import reduce

# define input
nums = [ 3, 24, 5, 8 ]

# find sum
sum_ = reduce (lambda x, y : x + y, nums)
print(sum_)

# find product
product = reduce (lambda x, y : x * y, nums)
print(product)

