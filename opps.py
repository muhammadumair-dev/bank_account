class Account:
    def __init__(self , bal , acc):
        self.balance =bal
        self.account_no =acc
    def debit(self , amount):
        self.balance -= amount
        print("rs",amount,"was debit")
        print("total balance", self.get_balance())
    def credit(self , amount):
        self.balance += amount
        print("rs",amount,"was credit")
        print("total balance", self.get_balance())
    def get_balance(self):
        return self.balance

            

acc1 =Account(10000 ,1234)
print(acc1.balance)
acc1.debit(1000 )
acc1.credit(500)


        