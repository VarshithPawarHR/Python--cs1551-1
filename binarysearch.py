list =[]

def readelements(list):
  count = int(input('enter the number of elements you want to insert'))
  for i in range(count):
    val = int(input('enter the element '))
    list.append(val)

readelements(list)

def binarsearch(list,n):
  list.sort()
  low =0
  high = len(list)-1
  mid =0

  while low<=high:
    mid = (low+high)//2

    if list[mid]<n:
      low = mid +1
    elif list[mid]>n:
      high = mid-1
    else:
      return mid
  return -1

key = int(input('enter the key u want to search'))
result = binarsearch(list,key)  

if result == -1:
  print('key not found')
else:
  print('key is found in the position',result)




