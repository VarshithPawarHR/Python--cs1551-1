
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("student.csv")
stdtotal=df.iloc[:,1::].sum(axis=1)
maxidx=stdtotal.idxmax()
maxtotal=stdtotal.max()
print("student usn:",df.iloc[maxidx,0])
print("marks=",maxtotal)
Sgrade=[]
Agrade=[]
Fgrade=[]
subcode=[]

for i in range(1,len(df.columns),2):
    total=df.iloc[:,[i,i+1]].sum(axis=1)
    Scount=Acount=Fcount=0
    for value in total:
        if value >= 90:
            Scount+=1
        elif 80 <= value < 90:
            Acount+=1
        elif value < 40:
            Fcount+=1
    Sgrade.append(Scount)
    Agrade.append(Acount)
    Fgrade.append(Fcount)
    code=df.columns[i][:5]
    subcode.append(code)

x1=[]
x2=[]
x3=[]
ticks=[]
w=0.2

for i in range(len(subcode)):
    x1.append(i)
    x2.append(i+w)
    x3.append(i+2*w)
    ticks.append(i+w)

plt.bar(x1,Sgrade,width=w,color='r',label="Sgrade")
plt.bar(x2,Agrade,width=w,color='g',label="Agrade")
plt.bar(x3,Fgrade,width=w,color='b',label="Fgrade")
plt.xticks(ticks,subcode)
plt.legend(loc="best")
plt.title("Course Grade Analysis")
plt.xlabel("Courses")
plt.ylabel("No Of Students")
plt.show()
