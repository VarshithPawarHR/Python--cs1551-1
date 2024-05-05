myfile = open('sample.txt', 'r')

linecount = 0
charcount = 0
wordcount = 0

for i in myfile:
    linecount += 1
    charcount += len(i)
    count = i.split()
    wordcount += len(count)

print("linecount is", linecount)
print("char count is ", charcount)
print("word count is", wordcount)
