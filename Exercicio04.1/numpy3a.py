import numpy as np
 
a = np.array([1,2,3])
print(a)

print a([0])
a[0] = 10
print(a)

b = a*np.array([2,0,2])
print(b)