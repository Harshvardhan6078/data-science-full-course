# functions are block of codes which takes some input do operation on it and give some output
# the internal working of function is hidden from user to reduce compleity 

def add(a,b):
    """
    this function returns the sum of  given numbers
    """
    sum = a+b
    print(sum)
    return sum

add(2,4)
add(34,56)

# parameters VS argument
# types of argumens --> ( default , positional , keyword)
# ------------------------------------------------------------------------------------------
# most important topic 
# *args and **kwargs

def sum(*args):   # this allow user to acces non keyword arguments

    """
    This function returns the sum of all given arguments

    """
    summation = 1
    for i in args:
        summation = summation + i
    return summation

print(sum(1,2,3,4,5,6,7,8,9,12,23,33,45,65,78))


# document access
print(sum.__doc__)    # important *****************************************************
print(print.__doc__)

# **kwargs ( allow us to pass any number of keywords arguments)
# keyword arguments means that they contain a key-value pair like a python dictionary

def dictionary(**kwarg):
    for (key,value) in kwarg.items() :
        print(key, '-->', value )

dictionary(india = 'delhi',srilanka = 'colombo' )

# the sequence is very imporant and fix while using multiple types of inputs -->( normal input --> *args --> **kwargs )  ****************

"""
When we create a function the function is executed separately from our original program ( It acts as a separate independent program)
The Life of A function exist only until it is called and it returns value after Function get executed 
the function from the RAM and variable inside it get destroyed automatically

"""
# without return value the default return is None 
# some functions dont have return value ( eg - list.uppend(9) --> permenant changes )

# variable scope

# local and global variable (locals can use global variables but cant change it)
# global keyword

# nested functions

# functions are 1st class citizens ( function in python are data type function)

# function is immutable data type

def f():
    def x(a,b):
        return a+b
    return x
val = f()(3,4)
print(val)


# print(funct_b(funct_a))   ********************************
# advantages of function
# code modularity
# code readibility
# code reusability


