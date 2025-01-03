import numpy as np


def f2c(temps):
    return (5 / 9) * (temps - 32)


fahrenheits = np.array([32, -4, 14, -40, 100, 105, 110, 115, 120, 125])
celsius = f2c(fahrenheits)
print('Celsius: {}'.format(repr(celsius)))


fahrenheits = np.arange(100, 125, 5)
print('fahrenheits : {}'.format(repr(fahrenheits)))
celsius = f2c(fahrenheits)
print('celsius : {}'.format(repr(celsius)))
