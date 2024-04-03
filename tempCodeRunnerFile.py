import matplotlib.pyplot as plt

f1=open("keys.txt")
line=f1.readline()
key=line.split()
f1.close()

f1=open("marks.txt")
mark=[]
name=[]
print("Total marks of each student is")
for line in f1:
    ans=line.split()
    total=0
    for i in range(1,len(ans)):
        if ans[i]==key[i-1]:
            total+=1
    print(ans[0],total)
    mark.append(total)
    name.append(ans[0])
high=max(mark)
index=mark.index(high)
print("Top Score:",high)
print("Top Scorer:",name[index])

#Computing the range
r1=r2=r3=0
for value in mark:
    if value>=0 and value<=2:
        r1+=1
    elif value>=3 and value<=6:
        r2+=1
    else:
        r3+=1
#plot the graph
x=["0-2","3-6","7-10"]
y=[r1,r2,r3]
w=0.1
plt.bar(x,y,width=w,color=['r','g','b'])
plt.title("Students Performance in MCQ")
plt.xlabel("Score Range")
plt.ylabel("No.of Students")
plt.show()