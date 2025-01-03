import pandas as pd

series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print('{}\n'.format(series))

series = pd.Series({'b': 2, 'a': 1, 'c': 3})
print('{}\n'.format(series))
