String1 = "Educative"
print("Characters between 3rd and 5th index: ")
print(String1[3:5])
print("Characters between 3rd and 3rd-last index: ")
print(String1[3:-3])

String2 = String1 + ' Learner'
print(String2)

String3 = String2[:9] + '-' + String2[10:]
print(String3)