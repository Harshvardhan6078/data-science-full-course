gmail = input("please enter gmail")
password = input("please enter password")


if gmail == "basudeharsh@gmail.com" and password == "60786078":
    print('you are welcome to the system')
elif gmail == "basudeharsh@gmail.com" and password != "60786078" :
    password = input("last chance to enter your correct password")
    if password == "60786078":
         print('you are welcome to the system')
    else :
        print("please mess with system")
else :
    print("your credentials are wrong")

