import matplotlib.pyplot as plt

f1 = open('keys.txt')
line = f1.readline()
key = line.split()
f1.close()

f1 = open('marks.txt')
mark =[]
name = []

for line in f1:
  total =0
  ans = line.split()
  for i in range(1,len(ans)):
    if ans[i] == key[i-1]:
      total+=1
  print(ans[0],total)
  mark.append(total)
  name.append(ans[0])
high = max(mark)
index = mark.index(high)
print("max marks is: ",high)
print("max scorer is :", name[index])

r1=r2=r3=0
for values in mark:
  if values>=0 and values<=2:
    r1+=1
  if values>=3 and values<=6:
    r2+=1
  else:
    r3+=1

x =["0-2","3-6","7-10"]
y =[r1,r2,r3]

plt.bar(x,y,width=0.1,color = ['r','g','b'])
plt.title('students performance in mcq test')
plt.xlabel('score range')
plt.ylabel('no of students')
plt.show()
