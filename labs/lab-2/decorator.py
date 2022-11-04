import time

def calculate_time(function):
    def wrap(n):
        start = time.time()
        result = function(n)
        end = time.time()
        return result, end - start
    return wrap

@calculate_time
def sum1(n):
   result = 0
   for i in range(1, n + 1):
      result += i
   return result

if __name__ == '__main__':
    n = 1000000
    s, t = sum1(1000000)
    print(f'It took {t} sec.')
    print(f'The sum of numbers from 1 to {n} is {s}.')
