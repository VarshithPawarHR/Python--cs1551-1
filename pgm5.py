str1 = input("enter the string")

count = 0

for i in range(len(str1)):
    if str1[i].isupper():
        count += 1
        print("capital letter ", str1[i], "is present in position", i+1)

print("number of upper case letters is ", count)
