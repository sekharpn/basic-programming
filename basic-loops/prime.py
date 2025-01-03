num = int(input("Enter the input:"))
countFactor = 0
for i in range(1, num + 1):
    if num % i == 0:
        countFactor += 1

if countFactor == 2:
    print(num, " is a prime number")
else:
    print(num, " is not a prime number")