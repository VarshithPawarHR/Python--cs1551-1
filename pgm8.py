str1 = input("enter string 1 ")

str2 = input("enter string 2 ")

str3 = str1+str2

outstr = ""

for ch in str3:
    if ch.isupper():
        outstr = outstr + ch

print("output is ", outstr)
