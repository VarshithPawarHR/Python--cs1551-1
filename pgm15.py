class country:
    def __init__(self, name, capital, population):
        self.__name = name
        self.__capital = capital
        self.__population = population

    def display(self):
        print('capital : ', self.__capital)
        print("population : ", self.__population)


cname = []
clist = []
plist = []


while True:
    print("enter a choice \n")
    print("1.enter the info \n 2.display \n 3.highest population \n 4.exit \n")

    choice = int(input("enter please "))

    if choice == 1:
        name = input("enter the country name")

        if name in cname:
            print("info already exists ")
        else:
            capital = input("enter capital name")
            population = int(input("enter population "))

            new = country(name, capital, population)
            clist.append(new)
            cname.append(name)
            plist.append(population)

    elif choice == 2:
        name = input('enter the countries name : ')

        if name in cname:
            index = cname.index(name)
            print("details : ")
            clist[index].display()
        else:
            print("no data on the entered country")

    elif choice == 3:
        if len(plist) == 0:
            print("no data in the db")
        else:
            high = max(plist)
            index = plist.index(high)

            print("highest population is ", high,
                  " country with highest population is ", cname[index])
    else:
        break
