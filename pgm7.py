punstr = "’!()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~"

str1 = input("enter the string ")

outputstr1 = ""

for ch in str1:
    if ch not in punstr:
        outputstr1 += ch

print("out put is", outputstr1)
