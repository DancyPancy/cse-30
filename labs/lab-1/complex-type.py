num1, num2, num3, num4 = 125, 21, 30, 16

# complex numbers
cnum1 = complex(num1, num2)
cnum2 = complex(num2, num4)
print(cnum1, cnum2)

# conj(x1+y1*i)  = x1-y1*i  
print(cnum1.conjugate())   

# (x1+y1*i) + (x2+y2*i)  = (x1+x2)+(y1+y2)*i 
print(cnum1 + cnum2) 

#(x1+y1*i)*(x2+y2*i) = (x1*x2-y1*y2)+(x1*y2+y1*x2)*i
print(cnum1 * cnum2) 

# (x1+y1*i)/(x2+y2*i) = [(x1*x2+y1*y2)+(y1*x2q-x1*y2)*i] /(x2*x2+y2*y2)
print(cnum1 / cnum2)