lst = []


def smallindex(lst):
    small = min(lst)
    index = lst.index(small)
    return small, index


count = int(input("enter the size of list"))

for ch in range(count):
    val = int(input("enter the list element"))
    lst.append(val)

small, index = smallindex(lst)

print("smallest element in the list is", small, "its index is ", index)
