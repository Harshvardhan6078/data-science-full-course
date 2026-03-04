# hetrogeneous data types = [1,'jesus',[30,40,50]]
# list act like dynamic array
# fatch using list[1], list[2]

# arry are fixed sized but list are not
# less speed of eecution and more memory taken by list
# list actually store id of values not actual values (reference address)
# also called referential array

# characterstics of list
# ordered
# mutable
# hetrogeneous
# can have duplicate
# dynamic
# can be nested
# items can be accessed
# can contain any type of python object

L = [1,2,3,4,5,4,3,2,4]
L1 = [1,2,3,4,5,4,3,2,4]
print(L1 == L)

#creating list
#empty list
L2 = []
L3 = [1,2,3]         # 1d list
L4 = [1,2,[1,2,3]]   # 2d list ......
L5 = [[[1,2,3,4]]]   # 3d list
L6 = ['hello']
print(L6)
print(list('hello'))


# indexing and slicing --> positive indexing , negative indexing , 

l1 = [1,2,3,4,5,6,6,7,8,9]
print(l1[-1])
print(l1[5])
print(l1[-1:1:-2])
print(l1[1:6:3])

l2 = [1,2,3,[1,2,3],[7,8,9,[4,6,7]]]
print(l2[-1][-1][1])


print('######################################################################3')

l2.append(7)             # to insert only one item
print(l2)                 
l2.extend([1,2,3,4,5])   # extend multiple items
print(l2)
l = [1,2,3,[1,2,3,4],'hello','nikal na bsdk',2.17]
l2.extend(l)
print(l2)
l2.extend('delhi')
print(l2)
l2.append('hello')
print(l2)
l2.insert(1,[1,2,3,'hello world'])
print(l2)


# editing (replacing)
l1[1]=500 # through indexing
l1[2:5] = [0,9,5]
print(l1)

# use of del to delete

del l1[1]
del l2[6::2]
print(l1,l2,end='\n')

# remove removing without telling index
l2.remove(5)
print(l2)

# pop
l1.pop(3)   # here we gave inde but default is last value of list
l1.pop()

l1.clear()  # enpty whole list
print(l1)


# -----------------------------------------------------------------------------------------------------
#operations on list
# arithmatic operators (+ , *)
# membership operators
# loops

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print(l,l2,sep='\n')
print(l+l2)           # (just like concatination merge into one list)
print(l*4)            # repeat numbers 4 times

print(1 in l2)


#----------------------------------------------------------------------------------------------------------------------------

# loops in list

for i in l2:
    print(i)

# --------------------------------------------------------------------------------------------------------------------------

# functions in loops
# len/ min/ max/ sorted, sum( universal)
print(len(l2))
print(l2.index(3))

#---------------------------------------------------------------------------------------------------------------------
# l.reverse() (permenant operation)
# l.sort() permenant
#sorted(l) (temperory operation)
# l1.copy()