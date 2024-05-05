str1 = input("enter string 1")

str2 = input("enter string 2")

str3 = str1 + str2

outputstr1 = ""

for ch in str3:
    if ch.isupper():
        outputstr1 += ch

print("output is ", outputstr1)
