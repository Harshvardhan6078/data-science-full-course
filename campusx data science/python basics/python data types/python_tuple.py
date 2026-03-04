# tuple ( same like list but immutable)
# immutable
# hetrogeneous , fix size , 
# difference between list and tuple (synta, mutability, speed, memory, built in functions, error prone, usability )

tup0 = ()
tup1 = (1,) # for single value tuple
print(type(tup1))

tup2 = (1,2,3,4,5,6)
print(tup2)

tup3 = (1,2,3,[4,5,6],(9,8,7))
print(tup3)

l1 = list('hello')
print(l1)

tup4 = tuple('harshvardhan')
print(tup4)


#------------------------------------------------------------------------------------------------------
# accessing items 1. indeing  , 2. slicing

tup5 = (1,2,3,4,5,6,7,8,8,6,3,4)
print(tup5[3])                    # indexing
print(tup5[-1])
print(tup5[1:-1])
print(tup5[-1:1:-1])

# operations on tuples
# + and *
print(tup3+tup4)
print(tup3*2)

# membership
print(5 in tup4)
print(4 not in tup2)


# loops

for i in tup5:
    print(i)

# functions in tuples
# len, sum, min, max, sorted, count, index
print(type(sorted(tup5,reverse=True)))   # op is list
print(tup5.count(5)) # count of 5 


#---------------------------------------------------------------------------------
# tuple comprehension
tup6 = tuple(i*2 for i in tup5 if i%2==0)
print(tup6)


#-----------------------------------------------------------------------------------------------------------------
# tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)

a,b,*others = (1,2,3,4,5,6,7)
print(a,b,others)

#------------------------------------------------------------------------------------------------------------
# zipping

a = (1,2,4,7)
b = (2,5,8,9)

print(zip(a,b))
print(tuple(zip(a,b)))