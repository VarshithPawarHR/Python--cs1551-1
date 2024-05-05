import matplotlib.pyplot as plt

f1 = open('keys.txt')
line = f1.readline()
key = line.split()
f1.close()

f1 = open('marks.txt')

name = []
mark = []

for line in f1:
    ans = line.split()
    total = 0
    for i in range(1, len(ans)):
        if ans[i] == key[i-1]:
            total += 1
    print("total :", ans[0], total)
    name.append(ans[0])
    mark.append(total)

high = max(mark)
index = mark.index(high)
print("top score is ", high)
print("top scorer is ", name[index])


r1 = r2 = r3 = 0

for value in mark:
    if value >= 0 and value <= 2:
        r1 += 1
    if value >= 3 and value <= 6:
        r2 += 1
    else:
        r3 += 1

x = ["0-2", "3-6", "7-10"]
y = [r1, r2, r3]

plt.bar(x, y, width=0.1, color=['r', 'g', 'b'])
plt.title("i dont know the title")
plt.xlabel("something xxx")
plt.ylabel("something yyyy")
plt.show()
