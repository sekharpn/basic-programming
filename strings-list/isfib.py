fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4182]
count = 2
fibFlag = 1
while count < len(fib) and fibFlag == 1:
    if fib[count] != fib[count-2] + fib[count-1]:
        fibFlag = 0
    count += 1
if fibFlag == 0:

    print ("It's not a Fibonacci sequence due to the value", fib[count-1], "at index", count-1)
else:
    print ("Hurrah ... we've got a Fibonacci sequence.")
