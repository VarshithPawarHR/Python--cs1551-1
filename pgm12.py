file = input("enter the file name \n")

f1 = open(file)

count = 1

for i in f1:
    line = i.split()
    sum = 0
    for marks in line:
        sum = sum + int(marks)
    avg = sum / len(line)
    print("student ", count, "marks is \n")
    print("total ", sum)
    print("average is ", avg)
    print("------------------------------------------")
    count += 1
