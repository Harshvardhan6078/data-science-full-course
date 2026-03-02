print("please enter following values")
a , b , c = int(input("a")),int(input("b")),int(input("c"))

if a > b :
    if a > c :
        print(a, " is a and greatest ")
    else :
        print(c, " is c and greatest")
else :
    if b > c :
        print(b,"is b and greatest")
    else :
        print(c,"is c and greatest")
