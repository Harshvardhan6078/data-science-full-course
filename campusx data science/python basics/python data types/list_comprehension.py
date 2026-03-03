# a simplear way to create list with conditions
# newlist = [expression for item in iterable if condition == True]

l = [i for i in range(1,11)]
print(l)

for i in l:
    print(i)

s = -3
v = [ i*s for i in l]
print(v)

x = [i for i in range(1,51) if i%5==0]
print(x)

lang =['java','python','php','c','javascript','docker']
g = [i for i in lang if i[0]=='j']
print(g)

g1 = [i for i in lang if i.startswith('p')]
print(g1)

#----------------------------------------------------------------------------------------------------------------

basket = ['apple','banana','cherry','guava']
my_basket = ['apple','kiwi','graps','banana']

lk = [i for i in my_basket if i in basket and i.startswith('a')]
print(lk)

h = [[i*j for i in range(1,4)] for j in range(1,4)]
print(h)



#-----------------------------------------------------------------------------------------------------------------
# list traversing

for i in lk:
    print(i)   # itemwise


for i in range(0,len(l)):
    print(l[i])

#----------------------------------------------------------------------------------------------------------------
# zip

