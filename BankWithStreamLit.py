import streamlit as st
st.title("bank application")

class Bank :
    def __init__(self,bal,pin):
        self.bal = bal
        self.pin = pin
        self.op=3
    def Pin(self):
        k=3
        while True:
            k -= 1
            y = int(st.text_input("Enter the pin","0"))
            if y != self.pin:
                st.write("Entered invalid pin number")
                st.write("You have ", k, " Chances left")
            else:
                st.write("You entered valid pin")
                break
            if k == 0:
                st.write("Your card has blocked")
                exit(0)
    def Deposit(self,amount) :
        if amount>=100 and amount<=50000 and amount%100==0 :
            self.bal+=amount
            st.write("The total balance is ",self.bal)
        else :
            st.write("The amount should be not less than 100 ,not more 50k and it should be multiples of 100")
    def Withdraw(self,amount) :
        amt = self.bal-amount
        if amount>=100 and amount%100==0 and amount<=20000 :
            if self.op==0 :
                st.write("You cannot withdraw more than 3 times in a day")
                return
            if amt<=500 :
                st.write("Minimum balance should be maintained")
                return
            if amount>self.bal :
                st.write("Insufficient balance")
                return
            st.write("Withdrawal of ",amount," is success")
            self.bal-=amount
            st.write("The remaining is ",self.bal)
            self.op -= 1
        else :
            st.write("The withdraw amount should be between 100 and 20k and the amount should be multiples of 100")
    def BalanceEnquire(self) :
        ("The available amount is ",self.bal)
    def EXIT(self) :
        st.write("You Choose to exit")
        exit(0)

st.write("Welcome to ABC Bank")
m = Bank(10000,1234)
m.Pin()

st.write("The options are")
st.write("1. Deposit\n2. Withdraw\n3. Balance Enquire\n0. EXIT")

while True :
    choice = st.number_input("\nEnter the operation",min_value=0)
    match choice :
        case 1 :
            n = st.number_input("Enter the amount to be deposited\n")
            m.Deposit(n)
        case 2 :
            n=st.number_input("Enter the amount to be withdrawn\n")
            m.Withdraw(n)
        case 3 :
            m.BalanceEnquire()
        case 4 :
            m.EXIT()