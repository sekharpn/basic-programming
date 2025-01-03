import numpy as np

arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

reshaped_arr = np.reshape(arr, (-1, 2, 2))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

arr1 = np.arange(9, dtype=np.int32)
print(repr(arr1))

reshaped_arr1 = np.reshape(arr1, (3,3))
print(repr(reshaped_arr1+1))
