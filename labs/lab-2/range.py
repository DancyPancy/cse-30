# x = list(range(1000))         # x = [0, 1, 2, …, 999], x is a list of 1000 numbers
# for k in x:
#     print(k)
# print(type(x))

# y = range(1000)
# for k in y:
#     print(k)
# print(type(y))

def my_range(stop, start=0, step=1):
    n = start
    print(start, stop, step)
    while (n < stop and step > 0) or (n > stop and step < 0):
        yield n
        n += step

# for k in my_range(10):
#     print(k, end=" ")

# note that the order of arguments (stop, start, step) is different
# from the built-in function range order (start, stop, step)!!! 
for k in my_range(0, 10, -1):  
    print(k, end=" ")