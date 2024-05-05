stud = {'john': 86.5, 'jack': 91.2, 'jill': 84.5, 'harry': 72.1, 'joe': 80.5}

total = sum(stud.values())
print("total marks scored by all", total)
average = total/len(stud)
print("average score is ", average)

count = 0

sortedlist = sorted(stud, key=stud.get, reverse=True)
for i in sortedlist:
    print("top scorer",count +1," is", i, "score", stud[i])
    if count == 2:
        break
    count += 1
