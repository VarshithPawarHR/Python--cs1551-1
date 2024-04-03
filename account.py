class Account:

    def __init__(self,number):
        self.number=number
        self.balance=100
       
    def deposit(self,amount):
        self.balance+=amount
        print("Account balance is:",self.balance)
       
    def withdraw(self,amount):
        if self.balance-amount<100:
            print("low balance for withdrawal")
        else:
            self.balance-=amount
            print("Account balance:",self.balance)
           
    def getbalance(self):
        return self.balance
   
acclist=[]
accnolist=[]

while True:
    print("Enter")
    print("1:Account creation\n2:Deposit\n3:Withdraw")
    print("4:Get highest balance\n5:exit")
    choice=int(input("Enter your choice\n"))
    if choice==1:
        number=int(input("enter the account no\n"))
        if number in accnolist:
            print("Account already exists")
        else:
            new=Account(number)
            acclist.append(new)
            accnolist.append(number)
           
    elif choice==2:
        number=int(input("enter the account no\n"))
        if number in accnolist:
            amount=float(input("Enter the amount for deposit\n"))
            index=accnolist.index(number)
            acclist[index].deposit(amount)
        else:
            print("account not found\n")
           
    elif choice==3:
        number=int(input("enter the account no\n"))
        if number in accnolist:
            amount=float(input("Enter the amount for withdrawal\n"))
            index=accnolist.index(number)
            acclist[index].withdraw(amount)
        else:
            print("account not found\n")
           
    elif choice==4:  
           ballist=[]
           for object in acclist:
               ballist.append(object.getbalance())
           if len(ballist)==0:
               print("No account exists")
           else:
               high=max(ballist)
               index=ballist.index(high)
               print("Highest balance value:",high)
               print("Account number is:",accnolist[index])
               
    else:
        break;