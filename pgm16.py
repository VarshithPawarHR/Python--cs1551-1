import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('student.csv')

avgsrs = pd.Series()

for i in range(1, len(df1.columns), 2):
    code = df1.columns[i][:5]
    avg = (df1.iloc[::, i].mean(0)+df1.iloc[::, i+1].mean(0))/2
    avgsrs[code] = avg


print("average score is ", avgsrs.max())
print("subject code with highest ", avgsrs.idxmax())

avgcie = df1.iloc[::, 1::2].mean(1)
avgsee = df1.iloc[::, 2::2].mean(1)

x1 = []
x2 = []
ticks = []

usn = df1['USN']
w = 0.2

for i in range(len(usn)):
    x1.append(i)
    x2.append(i+w)
    ticks.append(i+w/2)

plt.figure(figsize=(10, 5))
plt.bar(x1, avgcie, width=w, color='r', label='avgcie')
plt.bar(x2, avgsee, width=w, color='g', label='avgsee')
plt.xticks(ticks, usn)
plt.xlabel('students usn')
plt.ylabel('cie vs see')
plt.legend()
plt.show()
