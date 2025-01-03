import numpy as np

print(np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in a OverflowError: If we uncomment line 12 and run again.
# np.array([np.inf, 3], dtype=np.int32)
np.array([np.inf, 3], dtype=np.float32)
