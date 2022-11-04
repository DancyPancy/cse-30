# Note the pattern: (lambda parameters : expression) (*argv)
result = (lambda x, y : x + y) (2, 3)
print(result)

# save a lambda fxn into a variable!!!
# notice that we do not use the function definition!
sum = lambda x, y : x + y
result = sum (4, 3)
print(result)

# returns True or False depending on the number
is_even = lambda x : True if x % 2 == 0 else False
result = is_even ( 4 )
print(result)