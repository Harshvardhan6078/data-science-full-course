# nested loops are loops inside loops
# break , continue , pass

for i in range(1,11):
    for j in range(1,(i+1)):
        print("*",end="")
    print()


for i in range(0,11):
    for j in range(0,(i+1)):
        print(j,end="")
    print("")

for i in range(0,11):
    for j in range(0,(i)):
        print(j,end="")
    for k in range(i,-1,-1):
        print(k,end="")
    print()


n = int(input("please enter the range "))
for i in range(2,n):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)

    