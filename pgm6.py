str = input("enter the string \n")

acount = ecount = icount = ocount = ucount = 0

str = str.lower()

for i in str:
    if i == 'a':
        acount += 1
    if i == 'e':
        ecount += 1
    if i == 'i':
        icount += 1
    if i == 'o':
        ocount += 1
    if i == 'u':
        ucount += 1

print("number of vowels `a` is", acount)
print("number of vowels `e` is", ecount)
print("number of vowels `i` is", icount)
print("number of vowels `o` is", ocount)
print("number of vowels `u` is", ucount)
