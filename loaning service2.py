#Bank contains record of transactions and members
class Bank():
    _ledger=[] # list of transactions, to be accessed only by bank objects
    members={} # dictionary with members and their balance

#Every time a member becomes a lender, lender class is used    
class lender(Bank):
    def __init__(self,name,balance):
        #constructor for lenders
        self.name=name
        self.balance=balance
    # method for lending
    def lend(self,user2,amt):
        if self.set_balance(-amt):
            user2.set_balance(amt)
            return self.name+" gave "+str(amt)+" to "+user2.name #records transaction
        else:
            return "bounce"
    #method to update bank balance
    def set_balance(self,amt):
        if self.members[self.name]+amt<0:
            print("Not enough cash")
            return 0
        self.members[self.name]+=amt
        return 1
#Every time a member becomes a borrower,borrower class is used
#Logic used in borrower is mostly same as lender
class borrower(Bank):
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def borrow(self,user2,amt):
        self.set_balance(amt)
        user2.set_balance(-amt)
        return user2.name+" gave "+str(amt)+" to "+self.name
    def set_balance(self,amt):
        self.members[self.name]+=amt

print("""        Welcome to Loaning services\n
        Controls\n
        su -Sign up\n
        h -check history\n
        l -lend\n
        b -borrow\n
        exit -exit service portal""")       
inpt=" "

bank=Bank() # bank object that will track all transactions and members

while(inpt!="exit"):
    inpt=input("-->")
    if inpt=="su":
        user=input("Enter id:")
        balance=int(input("Enter balance:"))
        bank.members[user]=balance
    elif inpt=="l":
        user1=input("Lender id:")
        user2=input("Giving to:")
        amt=int(input("Amt:"))
        u1=lender(user1,bank.members[user1]) #user acting as lender
        u2=borrower(user2,bank.members[user2])
        bank._ledger.append(u1.lend(u2,amt))
    elif inpt=="b":
        user1=input("Borrower id:")
        user2=input("Taking from:")
        amt=int(input("Amt:"))
        u1=borrower(user1,bank.members[user1])#user acting as borrower
        u2=lender(user2,bank.members[user2])
        bank._ledger.append(u1.borrow(u2,amt))
    elif inpt=="h":
        user=input("Enter id:")
        print("Balance:",bank.members[user])
        print("History:")
        # history of the entered user will be shown
        for i in bank._ledger:
            if user in i:
                print(i)
        
        
        
    
