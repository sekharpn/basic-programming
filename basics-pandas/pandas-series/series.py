import pandas as pd
import numpy as np

# Creating an empty series, will result in DeprecationWarning
#series = pd.Series()

# Passing dtype as a parameter to Series for an empty series to avoid DeprecationWarning
# Creating an empty series
series = pd.Series(dtype='float64')
# Newline to separate series print statements
print('{}\n'.format(series))
