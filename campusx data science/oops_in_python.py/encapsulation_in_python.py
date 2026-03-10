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


        # instance and static variable
        # decorator   ############################## utility function
        # reference variable , pass by reference
        # mutability of object
        # encapsulation
        # collection of objects
        # instance variable
        # static variables         ****************************** 

        # 1. Instance Variables
            # Definition

            # An instance variable belongs to a specific object (instance) of a class.
            # Each object has its own copy.
            # Changes affect only that object, not others.
            # Defined using self inside methods (usually inside __init__). 
            # objectname.variable name = value ------------> instnce variable


         # 2. Static Variables (Class Variables)
         # Definition

                # A static variable is shared by all objects of the class.
                # Stored once in the class
                # Every object uses the same variable
                # Defined outside methods but inside class
                # self.cid = classname.variablename  -----------------> way to creat static variable


        # @staticmethod ------> decorator
        # static methods   ( can be without self ------> to access it use class name eg --> bank.get_counter())
        # utility method
        


        