punstr = "’!()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~"

inputstr = input("enter the string")

outputstr = ""

for ch in inputstr:
    if ch not in punstr:
        outputstr = outputstr + ch

print("output is :", outputstr)
