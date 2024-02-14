myfile = open('sample.txt','r')
linecount =0
charcount =0
count =0

for i in myfile:
  linecount = linecount+1
  charcount += len(i)
  wordcount = i.split()
  count += len(wordcount)

print('number of lines is', linecount)
print('number of characters is',charcount)
print('word is ',count)
