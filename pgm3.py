n = int(input("enter the number upto which you want the fib series"))

fib0, fib1 = 0, 1

if n <= 0:
    print("invalkid range")
else:
    if n == 1:
        print(fib0)
    else:
        print(fib0, fib1, end=" ")
        for i in range(1, n-1):
            fib3 = fib1+fib0
            print(fib3, end=" ")
            fib0 = fib1
            fib2 = fib3
