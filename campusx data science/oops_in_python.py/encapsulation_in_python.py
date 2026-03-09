# to make variables  , mthods private you just add __methodname 

class bank:

    def __init__(self):
        self.pin = ""
        self.__balance = 0                 # private variables

    def __ManagerMethod(self):             # private method even developer also cant see
        pass

    def _checkbalance(self):
        pass

person1 = bank()
print(dir(person1))

        # self.__balance
        # def __ManagerMethod()

        # Python converted them to:

        # _bank__balance
        # _bank__ManagerMethod



        # getter and setter
        