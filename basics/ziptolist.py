# create tuples with college
# id and name and store in a list
data = [(1, 'sravan'), (2, 'ojaswi'),
        (3, 'bobby'), (4, 'rohith'),
        (5, 'gnanesh')]

# display data
print(data)

# get first element using zip
print(list(zip(*data))[1])
print(list(zip(*data))[0])