#private
# class Account:

#     def __init__(self , acc_no , acc_pss):
#         self.acc_no = acc_no
#         self.__acc_pss =acc_pss
 
# acc1 = Account("1234" , "abcd")
# print(acc1.acc_no)
# print(acc1.__acc_pss)

# inheritance
class Car:
    @staticmethod
    def start ():
        print("car started..")
    @staticmethod
    def stop ():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self , name):
        self.name = name

car1 = ToyotaCar("forturener")
car2 =ToyotaCar("prius")
print(car1.name)
print(car2.name)
print(car1.start() ,car2.start())
print(car1.stop() ,car2.stop())

# multi inheritance

class Car:
    @staticmethod
    def start ():
        print("car started..")
    @staticmethod
    def stop ():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type =type

car1 =Fortuner("disel")
car1.start()
