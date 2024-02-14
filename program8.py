str1 = input('enter the string1')
str2 = input('enter string 2')
stri =''
strj =''

for i in str1:
  if i.isupper():
    stri = stri + i


for i in str2:
  if i.isupper():
    strj = strj + i


print('output is', stri+strj)