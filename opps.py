# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi",self.name , "your scro" , sum/3)
        
# s1 = Student("umair", [99 , 98 ,97])
# s1.get_avg()

        
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


        