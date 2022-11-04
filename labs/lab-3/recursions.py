# print numbers iteratively
def print_numbers(n):
    for i in range(1, n+1):
        print(i)
# main program
print_numbers(10)

# print numbers recursively
def print_numbers(n):
    if n == 1:           # the base case
        print(n)
    else:
      print_numbers(n-1) # recursive call
      print(n)
# main program
print_numbers(10)   