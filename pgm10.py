def smallindex(list):
    small = min(list)
    index = list.index(small)
    return small, index


list = []

count = int(input("enter the size of list"))
for ch in range(count):
    val = int(input("enter the values to list"))
    list.append(val)

smallele, index = smallindex(list)

print("smallest element is ", smallele)
print("its index is ", index)
