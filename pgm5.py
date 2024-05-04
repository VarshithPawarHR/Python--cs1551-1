str = input("enter the string")

count = 0

for i in range(len(str)):
    if str[i].isupper():
        count += 1
        print("capital letter ", str[i], "is present in position", i+1)

print("number of upper case letters is ", count)
