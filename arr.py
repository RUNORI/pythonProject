import numpy as np
#creation
a = np.array([2, 4, 6, 8])
print(a)

#slicing
b = a[0:4]
print(b)
c = a[:3]
print(c)
d = a[1:]
print(d)

#copying elemments frm 1 array to another
arr = a
print(id(arr))
a[1] = 7
print(a)
print(arr)