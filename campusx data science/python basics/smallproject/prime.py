# num = 111

# for i in range(2,num):
#     if num%i == 0:
#         print('not prime')
#         break
# else :
#     print('prime')


# for i in range()

# palindrome

num1 = 121

# a = 10
start =0
end= 1

def febo(a):
    global start, end 
    if start <= a:
        print(start)
        start , end = end , start+end
        febo(a)
    else:
        pass


febo(10)

a= 10
start = 0
last = 1
for i in  range(a):
    print(start)
    start , last = last ,start+last

