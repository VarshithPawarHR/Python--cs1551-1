file = input("enteer the file name")
f1 = open(file)

count = 1

for i in f1:
    line = i.split()
    sum = 0
    for mark in line:
        sum = sum + int(mark)
    avg = sum/len(line)
    print("student ", count, "details")
    print("total score is ", sum)
    print("average ", avg)
    count += 1
    print("---------------------------")
