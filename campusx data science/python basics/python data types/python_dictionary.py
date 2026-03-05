# dictionary is key value pair data type

dict1 = {'name': 'nitish', 'age':25, 'gnder':'male'}

# mutable
# no indexing
# keys cant be duplicate
# keys cant be mutable

d = {}  # empty dictionary
d1 = {'roll no':6078,'age':24}  # homogeneous
d2 = {'name':'harshvardhan','roll no': 6078 , 'marks':[78,88,92,90,96]}  # hetrogeneous

d3 = {
    'name' : 'harsh',
    'roll no' : 6078,
    'marks' : {                   # 2d dictionary
        'maths' : 88,
        'science' : 91,
        'english' : 91,
        'gk' : 70
        }
    }                            

print(d3)

d4 = dict([('name','nitish'),('age',24),(3,3)])
print(d4)
#-------------------------------------------------------------------------
d5 = {
    'names': ['harsh','basude','akshay','aditya','shital','arya'],
    'marks':[90,91,92,91,93,94]
}
print(d5)


# add new key
d5['gender'] = ['male','male','male','male','female','female']
print(d5)

#----------------------------------------------------------------------------
print(d5.pop('names'))
print(d5.popitem())
del(d1)
d2.clear()
print(d2)

d3['marks']['ds'] = 98
print(d3)

del d3['marks']['english']
print(d3)


d3['marks']['maths']=99
print(d3)

#------------------------------------------------------------------------------------------------

# dictionary operations
# membership, loops

d7 = {
    'name' : 'harsh',
    'roll no' : 6078,
    'marks' : {                   # 2d dictionary
        'maths' : 88,
        'science' : 91,
        'english' : 91,
        'gk' : 70
        }
    }                            



print('name' in d5)   # only work on keys not on values

for i in d7:
    print(i,d7[i])

print(len(d7))
print(sorted(d7))
print(max(d7))

# 4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

print(d7.items())
print(d7.keys)
print(d7.values())
# d2.update(d2)
# print(d1)


# dictionary comprehension

D1 = {i:i**2 for i in range(1,100)}
print(D1)


print('-----------------------------------------------------------------------------------------------------------')
# zip function

# nested comprehension
k = {i:{j:i*j for j in range(1,5)} for i in range(1,6) }
print(k) 