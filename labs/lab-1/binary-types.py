# make bytes
print(bytes(5)) # make 5 bytes equals to 0

print(bytes([97, 98, 99])) # make 3 bytes equals to 97, 98, 99

print(b'abc')    # using string, method 1

print('ア'.encode('utf-8')) # using string, method 2

print(bytes('abc', 'utf-8')) # using string, method 3

print('abc'.encode('utf-16-le'))

print(b'abc'.decode('utf-8'))

# bytes are not mutable
# a = bytes('abc', 'utf-8')
# a[ 1] = 102 # bytes are immutable!!! Write the error message, last line

# bytearray
print(bytearray(5))

print(bytearray([1, 2, 3]))

print(bytearray('abc', 'utf-16'))

# bytearray is mutable
b = bytearray('abc', 'utf-8')
print(b)

b[ 1]=114
print(b)

print('\n')
# convert into strings
a = bytes('abc', 'utf-8')
print(a)
print(a.decode('utf-8'))

b = bytearray('abc', 'utf-16-le')
print(b)
bytearray(b'a\x00b\x00c\x00')
print(b.decode('utf-16-le'))

# concatenate bytes and bytearray
print(a+b) # write the answer for the last print statement