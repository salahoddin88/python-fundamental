#class
class Home:
    # Attributes -> Variables
    # Behaviour -> Methods(function) function which is in the class are called methods
    #self, is variable which points to the instace of the class youare working with
    def room(self):
        print("2bhk")

#Object of an class
#Constructor
home = Home() 
home2 = Home() 

Home.room(home)
Home.room(home2)

home.room() # using object it self to call room 
# behind the scene this room will take room as a parameter and pass it to self.
a = 5
a.bit_length
exit()

class Customer():
    customerList = {'name':'salahuddin', 'card':'456', 'balance':50}
   
    def getCustomer(self):
        return self.customerList

    def updateBalance(self, balance = 0):
        self.customerList['balance'] = balance
        return self.customerList['balance']

    def checkCustomerCard(self, card):
        if self.customerList['card'] == card:
            return True
        return False

class ATM(Customer):

    def credit(self, amount):
        """ To credit amount in customer balance """
        customer = super().getCustomer()
        balance = int(customer['balance']) + int(amount)
        return super().updateBalance(balance)

    def debit(self, amount):
        """ To debit amount from customer balance """
        customer = super().getCustomer()
        balance = int(customer['balance']) - int(amount)
        return super().updateBalance(balance)

    def balace(self):
        return self.customerList['balance']


class Inputs:
    def card(self):
        return input('Card Number: ')

    def operation(self):
        return input(''' 
        1. credit
        2. debit
        3. balance
        4. exit
        Enter Your Choice : ''')

    def amount(self):
        return input('Amount : ')


atm = ATM()
customer = Customer()
atm.debit(50)
atm.credit(20)

inputs = Inputs()
operation = 0
while True:
    operation = int(inputs.operation())
    if operation == 4:
        break

    if operation == 3:
        balance = atm.balace()
        print(f'Current Balance : {balance}')
        continue

    card = inputs.card()
    
    if customer.checkCustomerCard(card):
        amount = inputs.amount()
        if operation == 1:
            balance = atm.credit(amount)
            print(f'Current Balance : {balance}')
        elif operation == 1:
            balance = atm.debit(amount)
            print(f'Current Balance : {balance}')
    else:
        print('Invalid Card')

#Method Resulation Order