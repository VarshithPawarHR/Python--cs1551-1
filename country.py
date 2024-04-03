class country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def display(self):
        print("Capital is", self.capital)
        print("Population is", self.population)

clist = []
cname = []
plist = []

while True:
    print("Choose:")
    print("1. Enter country details")
    print("2. Find country details")
    print("3. Find max population")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the country name: ")

        if name in clist:
            print("Country details already exist")
        else:
            capital = input("Enter the country capital: ")
            population = int(input("Enter the population: "))
            new_country = country(name, capital, population)
            cname.append(name)
            plist.append(population)
            clist.append(new_country)

    elif choice == 2:
        name = input("Enter country name: ")

        if name in cname:
            index = cname.index(name)
            print("Country details are:")
            clist[index].display()
        else:
            print("No details of the entered country")

    elif choice == 3:
        max_population = max(plist)
        index = plist.index(max_population)
        print("Country with maximum population is:", cname[index])

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please choose again.")
