list1 = []


def readelements(lst):
    n = int(input("enter the size of the list"))

    for i in range(n):
        val = int(input("enter the element "))
        lst.append(val)


readelements(list1)


def binarysearch(lst, n):
    lst.sort()
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low+high)//2

        if lst[mid] < n:
            low = mid + 1
        elif lst[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1


key = int(input("enter the value of key u want to search"))
result = binarysearch(list1, key)

if result == -1:
    print("key not found")
else:
    print("key is found at the index", result)
