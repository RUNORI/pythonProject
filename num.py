
import numpy as np

a = np.array([10,20,100,200,500])
b = np.array([3,4,5,6,7])
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a,b))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a : a + 10
print(x(5))
