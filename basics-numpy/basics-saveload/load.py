import numpy as np

arr = np.array([1, 2, 3])
np.save('arr.npy', arr)
load_arr = np.load('arr.npy')
print(repr(load_arr))

# Will result in a FileNotFoundError: If we uncomment line 9 and run again.
# load_arr = np.load('arr')
