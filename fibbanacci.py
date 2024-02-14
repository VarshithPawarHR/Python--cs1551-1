def fib(n):
  fibnext = [0,1]
  while(len(fibnext)<n):
    nextval = fibnext[-1]+fibnext[-2]
    fibnext.append(nextval)
  return fibnext[:n] 

n = int(input('enter the number who u want to fibacci series'))
print(fib(n)) 