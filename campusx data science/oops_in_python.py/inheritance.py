
# types of relationships in oops
      # aggrigation , inheritance 

# getter is the special type of method written in any class to give access of his private variables to
#  another class without showing that variable or keeping it private (abstraction , aggrigation relation)
# 

# parent class
class car:
    
    count = 0

    def __init__(self):
        self.speed = 160
        self.count = car.count + 1
    def wheels(self):
        pass

    def milage(self):
        print('milage is good')
        return 'milage is good'
    
    def start(self):
        print(' your car is started')
        

# child class of car
class tata(car):
    def __init__(self):
        self.model = 'safari'
        self.speed = 200
    
    def milage(self):
        return super().milage()
    
car1 = tata()
car1.start()