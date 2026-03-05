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