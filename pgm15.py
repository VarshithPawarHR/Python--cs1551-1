class country:
    def __init__(self, name, capital, population):
        self.__name = name
        self.__capital = capital
        self.__population = population

    def display(self):
        print("capital is ", self.__capital)
        print("population is ", self.__population)


clist = []
cname = []
plist = []

while True:

    print("enter your choice ")

    print("1.enter country detail \n 2.display \n 3.highest population \n 4.exit")
    choice = int(input("choose a option please "))

    if choice == 1:
        name = input("enter country name")

        if name in cname:
            print("info already exists")
        else:
            capital = input("enter capital")
            population = int(input("enter population"))

            new = country(name, capital, population)

            clist.append(new)
            cname.append(name)
            plist.append(population)

    elif choice == 2:
        name = input("enter country name")

        if name in cname:
            index = cname.index(name)
            clist[index].display()
        else:
            print("country does not exist")

    elif choice == 3:

        if len(plist) == 0:
            print("no information")
        else:
            high = max(plist)
            index = plist.index(high)
            print("country with highest population is", cname[index])
            print("population is ", high)

    else:
        break
