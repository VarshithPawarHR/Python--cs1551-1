str1 = input("enter the string")

outstr = ""

for ch in str1:
    if ch.isupper():
        outstr += ch

print("out put is", outstr)
