# return a Filter object (an iterator) that can be converted into a list
# define input
nums = [ 3, 24, 5, 8 ]

# apply filter
is_even = lambda x : True if x % 2 == 0 else False
even_filter = filter(is_even, nums)

# convert filter into list
even_list = list(even_filter)
print(even_list)

# or we can combine the filter code in one line
nums2 = [ 3, 2, 1 ]
even_list = list(filter(lambda x : True if x % 2 == 0 else False, nums2))
print(even_list)