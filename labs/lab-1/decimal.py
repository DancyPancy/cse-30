from decimal import *
num1, num2, num3, num4 = 125, 21, 30, 16

# decimal numbers
print(num1/num2)

getcontext().prec = 13   # set the decimal precision
dec1 = Decimal(num1)/Decimal(num2)
print(dec1)

getcontext().prec = 3   # note the precision!!!
print(dec1)

dec2 = Decimal(num3)/Decimal(num4)
print(dec2)