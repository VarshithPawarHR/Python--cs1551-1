
list1 =[]
list2 =[]

def readelements(list):
  count  = int(input('enter the value'))
  for i in range(count):
    val = int(input('entewr the elemenbts'))
    list.append(val)
  


readelements(list1)
readelements(list2)

def symmetric(list):
  evencount =0
  oddcount =0
  for i in list:
    if i%2==0:
      evencount +=1
    else:
      oddcount+=1
  return evencount,oddcount

evenlist1=0
evenlist2 =0
oddlist1 =0
oddlist2 =0

evenlist1,oddlist1 =symmetric(list1)
evenlist2,oddlist2 = symmetric(list2)

if(evenlist1==evenlist2&oddlist1==oddlist2):
  print('lists are symmetric')
else:
  print('list are unsymmetric')  
      

