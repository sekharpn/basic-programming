import numpy as np

arr = np.array([[0, 1, 2], [3, 4, 5]],
               dtype=np.float32)
print(repr(arr))

# elements of a NumPy array are mixed types, then the array's type will be upcast to the highest level type.
arr = np.array([0, 0.1, 2])
print(repr(arr))
