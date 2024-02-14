str = input('enter the string')
count =0

for i in range(len(str)):
  if str[i].isupper():
    count = count+1
    print(' the capital letter ',str[i] ,' is present at ',i+1,' position ')

print('total number of capital letters is ', count)
