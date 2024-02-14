stud = {'john':86.5,'jack':91.2,'jill':84.5,'harry':72,'joe':80.5}

total = sum(stud.values())
print('total marks of all students is',total)
average = total / len(stud)
print('average is',average)

sortedlist = sorted(stud,key = stud.get,reverse=True)

count =0
for i in sortedlist:
  print('top scorer' ,i , ': ', stud[i])
  if(count==2):
    break
  count +=1


