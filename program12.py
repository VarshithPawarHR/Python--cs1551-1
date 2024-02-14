filename = input('Enter the filename: ')
file = open(filename, 'r')
count = 1

for line in file:
    llist = line.split()
    total = 0  
    for mark in llist:
        total += int(mark)
    average = total / len(llist)

    print('Total marks of student', count, 'is', total)
    print('Average of', count, 'is', average)

    count += 1  
