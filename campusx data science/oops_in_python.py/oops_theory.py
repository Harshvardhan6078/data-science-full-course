    # class , objects , methods , constructor --> only one constructor per class
    # predefined and user defined class
    # class diagram ( attributes / data / variables , methods)
    # private , public methods
    # magic methods  ( dunder methods)   __ method__
                        # called automatically when object is created
                        # 
    # self is nothing but object itself eg - person1 = bank()   so  def withdera(self)   here self == person1

    # how to accces attributes
    # how to access methods
    # attribute creation ouside the class 
    # reference variables ( it is just pointer pointig to memory location)
    # creating multiple references dont create multiple variables

class person :

    def __init__(self):
        self.name = ''
        self.age = int()


p1 = person()
p1.name = 'harshvardhan'
p1.age = 24
print(p1.age, p1.name)
p1.language = "marathi"  # creating attribute of object outside the class  ( but it will be for just p1 not universal)

print(p1.language) 

# passing function as attribute

def greet (person):                                        # passing whole class as input
    print('my name is',person.name,'i am',p1.age)
greet(p1)



def greet (person1):                                     # passing just 1 object of class
    print('my name is',p1.name,'i am',p1.age)
greet(p1)                                                # everything will depend here


# objects of python are mutable by default
