class Bank():
    _ledger=[]
    members={}
    

class lender(Bank):
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def lend(self,user2,amt):
        if self.set_balance(-amt):
            user2.set_balance(amt)
            return self.name+" gave "+str(amt)+" to "+user2.name
        else:
            return "bounce"
    def set_balance(self,amt):
        if self.members[self.name]+amt<0:
            print("Not enough cash")
            return 0
        self.members[self.name]+=amt
        return 1
        
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
        b -borrow""")       
inpt=" "
while(inpt!="exit"):
    bank=Bank()
    inpt=input("-->")
    if inpt=="su":
        user=input("Enter id:")
        balance=int(input("Enter balance:"))
        bank.members[user]=balance
    elif inpt=="l":
        user1=input("Lender id:")
        user2=input("Giving to:")
        amt=int(input("Amt:"))
        u1=lender(user1,bank.members[user1])
        u2=borrower(user2,bank.members[user2])
        bank._ledger.append(u1.lend(u2,amt))
    elif inpt=="b":
        user1=input("Borrower id:")
        user2=input("Taking from:")
        amt=int(input("Amt:"))
        u1=borrower(user1,bank.members[user1])
        u2=lender(user2,bank.members[user2])
        bank._ledger.append(u1.borrow(u2,amt))
    elif inpt=="h":
        user=input("Enter id:")
        print("Balance:",bank.members[user])
        print("History:")
        for i in bank._ledger:
            if user in i:
                print(i)
        
        
        
    
