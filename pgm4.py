stud = {'jack': 87.9, 'jill': 99, 'varshith': 100, 'ravi': 45, 'afaik': 89}

total = sum(stud.values())

print("total marks scored by all students is ", total)
average = total / len(stud)
print("average is ", average)

sortedlist = sorted(stud, key=stud.get, reverse=True)

count = 0
print(":top scorers are \n")
for i in sortedlist:
    print("top score ", i, "is", stud[i])
    if count == 2:
        break
    count += 1
