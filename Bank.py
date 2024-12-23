class Bank :
    def __init__(self,bal,pin):
        self.bal = bal
        self.pin = pin
        self.op=3
    def Pin(self):
        k=3
        while True:
            k -= 1
            y = int(input("Enter the pin\n"))
            if y != self.pin:
                print("Entered invalid pin number")
                print("You have ", k, " Chances left")
            else:
                print("You entered valid pin")
                break
            if k == 0:
                print("Your card has blocked")
                exit(0)
    def Deposit(self,amount) :
        if amount>=100 and amount<=50000 and amount%100==0 :
            self.bal+=amount
            print("The total balance is ",self.bal)
        else :
            print("The amount should be not less than 100 ,not more 50k and it should be multiples of 100")
    def Withdraw(self,amount) :
        amt = self.bal-amount
        if amount>=100 and amount%100==0 and amount<=20000 :
            if self.op==0 :
                print("You cannot withdraw more than 3 times in a day")
                return
            if amt<=500 :
                print("Minimum balance should be maintained")
                return
            if amount>self.bal :
                print("Insufficient balance")
                return
            print("Withdrawal of ",amount," is success")
            self.bal-=amount
            print("The remaining is ",self.bal)
            self.op -= 1
        else :
            print("The withdraw amount should be between 100 and 20k and the amount should be multiples of 100")
    def BalanceEnquire(self) :
        print("The available amount is ",self.bal)
    def EXIT(self) :
        print("You Choose to exit")
        exit(0)

print("Welcome to ABC Bank")
m = Bank(10000,1234)
m.Pin()

print("The options are")
print("1. Deposit\n2. Withdraw\n3. Balance Enquire\n4. EXIT")

while True :
    print("\nEnter the operation")
    choice = int(input())
    match choice :
        case 1 :
            n = int(input("Enter the amount to be deposited\n"))
            m.Deposit(n)
        case 2 :
            n=int(input("Enter the amount to be withdrawn\n"))
            m.Withdraw(n)
        case 3 :
            m.BalanceEnquire()
        case 4 :
            m.EXIT()