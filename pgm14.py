import matplotlib.pyplot as plt

f1 = open('keys.txt')
line = f1.readline()
key = line.split()
f1.close()

marks = []
name = []


f1 = open('marks.txt')

print("total marks scored by students")
for line in f1:
    ans = line.split()
    total = 0
    for i in range(1, len(ans)):
        if ans[i] == key[i-1]:
            total += 1
    print(ans[0], total)
    marks.append(total)
    name.append(ans[0])

high = max(marks)
index = marks.index(high)
print("total scorer is",name[index])
print("top score is",high)

r1 = r2 = r3 = 0

for value in marks:
    if value >= 0 and value <= 2:
        r1 += 1
    if value >= 3 and value <= 6:
        r2 += 1
    else:
        r3 += 1


x = ['0-2', '3-6', '7-10']
y = [r1, r2, r3]
plt.bar(x, y, width=0.2, color=['r', 'g', 'b'])
plt.xlabel('score range')
plt.ylabel("number of students")
plt.show()
