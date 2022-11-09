import numpy as np
x = np.arange(0, np.pi*2, 0.1)
y = np.cos(x)+ np.sin(x)


print(np.argmax(y))

print(y[np.argmax(x)])

print(x[np.where(y == max(y))[0][0]])

print(np.where(y == max(y))[0][0])