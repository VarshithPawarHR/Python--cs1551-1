def fib(n):
  fibi = [0,1]
  for i in range(n):
    nextval = fibi[-1]+fibi[-2]
    fibi.append(nextval)
  return fibi[:n]\

n = int(input("enter the number"))
print('fibanassci series is', fib(n))    