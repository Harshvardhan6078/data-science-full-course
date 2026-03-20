# # compiler , interpreter , 

# print("hello world")
# print(7)
# print(True)
# print("hello",1,2,3,4,True)
# print("hello",1,2,3,45, True,sep="\n")


# num1 = 10
# num2 = 10

# print(id(num1))
# print(id(num2))

# num2 = 20
# print(num1)

# print(id(num1),id(num2))
# # concept of swapping packing and unpacking


# # match keyword 


# # switch in python
# # partition method


# str1 = "python class is my best class"
# print(str1.split(" "))

# print(str1[::2])
# print(str1.partition('th'))
# str1.isprintable()


# list1 = [1,2,3,4,5,6]
# list1.append(12)
# list1.extend([1,2,3,4])
# list1.insert(-1,300)


# s1 = {1,2,3,4}
# s2 = {9,8,7,6}
# l1 = [5,6,7,8]

# s1.union(s1)



# name = 'harsh basude'
# namel1 = name.split()
# print(namel1)
# namel1.reverse()
# print(namel1)
# print(" ".join(namel1))

# deep and shallow copy




# intrative statements
# string formating         ******************(f-string , format method)
# transfer statements
# flow control statments  -----> conditional
                                # looping
                                # jump
                                # function/eception

# operators 
# types of function


# fact = 1
# num = 5

# for i in range(1,num+1):
#     fact = fact*i

# print(fact)


# positional argument
# access specifier and modifier
# interface in oops
#                 -----> when all methods are @


# str1 = 'harshvardhanbasude'
# D1 = {i:i for i in str1 }
# print(D1)

# print()

#


h = [1,2,3,4,5,6]
ans = lambda x : x*2
print(ans)

ans1 = map(lambda x : x*2 , h)
print(ans1)
print(list(ans1))
print(list(ans1))

ans2 = filter(lambda x : x%2==0  , h )
print(list(ans2))



"""

def add(a,b):
    if a<1:
        a = a-1
        b = b-1
        sum = a+b
        add(a,b)
    else :
        sum = a+b
        return sum

a = print(add(6,7))

"""