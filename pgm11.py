myfile = open('sample.txt', 'r')

charcount = 0
linecount = 0
wordcount = 0

for line in myfile:
    linecount += 1
    charcount += len(line)
    count = line.split()
    wordcount += len(count)


print(" line count is", linecount)
print("char count is ", charcount)
print("word count is ", wordcount)
