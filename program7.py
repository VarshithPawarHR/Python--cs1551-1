inpstr = input('enter the string')
pattern  ='’!()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~'
output =''

for i in inpstr:
  if i  not in   pattern:
    output = output + i


print(output)