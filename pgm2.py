list1 = []
list2 = []


def readelements(lst):
    n = int(input("enter the size of the list"))

    for count in range(n):
        value = int(input("enter the element"))
        lst.append(value)


readelements(list1)
readelements(list2)


def symmetric(lst):
    evencount = 0
    oddcount = 0

    for ch in lst:
        if ch % 2 == 0:
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

if even1 == even2 and odd1 == odd2:
    print("yes symmetric")
else:
    print("noooooooo")
