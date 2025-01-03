n = int(input("Enter the number of terms (maximum 20) for the Fibonacci sequence:"))
if (n < 2) or (n > 20):
    print("\n\nIt seems the number of terms for the Fibonacci sequence has an invalid value:", n)
else:
    fib = [0] * n
    print("\n\nFirst", n, "terms of Fibonacci sequence are:")
    if (n > 1):
        fib[1] = 1  # Assigning 1 to 2nd index of list fib
    count = 2
    while count < n:  # This loop will terminate when the count is not less than n
        fib[count] = fib[count - 2] + fib[count - 1]  # Adding last two values
        count += 1
    print(fib)

print("*** Finish generating Fibonacci Numbers ***")