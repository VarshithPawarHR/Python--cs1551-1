class Account:
    def __init__(self, number):
        self.__number = number
        self.__balance = 100

    def deposit(self, amount):
        self.__balance += amount
        print("balance is ", self.__balance)

    def withdraw(self, amount):
        if self.__balance-amount < 100:
            print("insufficient balance")

        else:
            self.__balance -= amount
            print("balance is ", self.__balance)

    def getbalance(self):
        return self.__balance


acclst = []
accnolst = []

while True:

    print("choose one option")

    print("1.create account \n 2.deposit \n 3.withdraw \n 4.highest amount \n 5.exit")

    choice = int(input("enter your choice"))

    if choice == 1:

        number = int(input("enter the account number"))

        if number in accnolst:
            print("account already exists")
        else:
            new = Account(number)
            acclst.append(new)
            accnolst.append(number)

    elif choice == 2:

        number = int(input("enter the account number"))

        if number in accnolst:
            amount = float(input("enter the amount"))
            index = accnolst.index(number)
            acclst[index].deposit(amount)
        else:
            print("no such account")

    elif choice == 3:
        number = int(input("enter the account number"))

        if number in accnolst:
            amount = float(input("enter the amount"))
            index = accnolst.index(number)
            acclst[index].withdraw(amount)
        else:
            print("no such account")
    elif choice == 4:
        ballst = []

        for object in acclst:
            ballst.append(object.getbalance())

        if len(ballst) == 0:
            print("no account")
        else:
            high = max(ballst)
            index = ballst.index(high)
            print("account number with maximum amount is ",
                  accnolst[index], "amounbt is ", high)
    else:
        break
