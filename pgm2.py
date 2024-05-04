def readelements(list):
    count = int(input("enter the size of the list"))
    for ch in range(count):
        val = int(input("enter the element "))
        list.append(val)


list1 = []
list2 = []

readelements(list1)
readelements(list2)


def symmetric(list):
    evencount = 0
    oddcount = 0
    for i in list:
        if i % 2 == 0:
            evencount += 1
        else:
            oddcount += 1
    return evencount, oddcount


even1 = 0
odd1 = 0
even2 = 0
odd2 = 0

even1, odd1 = symmetric(list1)
even2, odd2 = symmetric(list2)

if (even1 == even2 and odd1 == odd2):
    print("yes symmetric boy")
else:
    print("not symmetric")
