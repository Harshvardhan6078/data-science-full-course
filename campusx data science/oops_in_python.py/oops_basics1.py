class atm:
    def __init__(self):
        self.balance = 0
        self.pin = ''
        self.balance = int(input('please enter your balance'))
        self.pin = input('please enter your pin')
        self.menu()
    
    def menu(self):
        while True:
            # self.balance = int(input('please enter your balance'))
            # self.pin = input('please enter your pin')

            ip = int(input(" how can i help you please enter \n" \
            "1 to check balance \n" \
            "2 to withdraw \n" \
            "3 to depoite "))

            if ip == 1:
                self.bal_check()

            elif ip == 2:
                self.withdraw()

            elif ip == 3:
                self.deposite()


    def auth(self):
        pin = input('plase enter your pin')
        if pin == self.pin:
            return True
        else :
            print(' wrong pin ' \
            'you are not authorized to access this account')
            return False
            

    def bal_check(self):
        # self.auth()
        if self.auth() == True:
            print(' your balance is', self.balance)
            cont = input('do you want to continue with other service')
            if cont == 'yes' or cont == 'Yes' or cont == 'y' or cont == 'Y':
                self.menu()
            else :
                print('\n Thank you for using our service')
                exit()
        else :
            self.menu()


    def withdraw(self):
        wi = int(input('please enter amount to withdraw'))
        if wi <= self.balance:
            print(' take this your',wi)
            self.balance = self.balance - wi


            # cont = input('do you want to continue with other service')
            # if cont.lower() in ['yes','y']:
            #     self.menu()
            # else:
            #     print('Thank you')

            cont = input('do you want to continue with other service')
            if cont == 'yes' or cont == 'Yes' or cont == 'y' or cont == 'Y':
                self.menu()
            else :
                print('\n Thank you for using our service')
        else :
            print(' not enough balance ')

            
    def deposite(self):
        dep = int(input('please enter amount you want to deposite'))
        self.balance = self.balance + dep
        print('your amount has been deposited to your account')
        i = input("do you want to see balance \n for yes 'y' ")
        # print('your current balance is - ',self.balance if i == 'y' or 'Y' else self.menu)


        if i == 'y' or cont == 'Y' or cont == 'yes' or cont == 'Yes':
            print('your balance is -->', self.balance )
            cont = input('do you want to continue with other service')

            if cont == 'yes' or cont == 'Yes' or cont == 'y' or cont == 'Y':
                self.menu()
            else :
                print('\n Thank you for using our service')
                exit()


user = atm()
