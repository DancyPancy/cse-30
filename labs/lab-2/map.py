# return a map object (an iterator) that can be converted into a list
# define input
nums = [ 3, 24, 5, 8 ]

# apply map
cube = lambda x : x**3
cube_map =  map (cube, nums)
print(cube_map)

# convert map into list
print(list(cube_map))

nums2 = [ 3, 2, 1 ]
cube_list = list(map(lambda x : x**3, nums2))
print(cube_list)