n = int(input("enter the value of n \n"))

fib0, fib1 = 0, 1

if n <= 0:
    print("invalid range")
else:
    print("fibanacci series is : ")
    if n == 1:
        print(fib0, end=" ")
    else:
        print(fib0, fib1, end=" ")
        for i in range(3, n+1):
            fib3 = fib1 + fib0
            print(fib3, end=" ")
            fib0 = fib1
            fib2 = fib3
