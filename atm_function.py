#error 
"""
1. We can not have same function name definition and declaration with variables name 
2. After chaning the name we had this code *print(f"Current Balance : {(balance)}")* it should be *print(f"Current Balance : {balance}")*
*balance* without parentheses
"""



customer = {'name' : 'Nikhil', 'card':'123456', 'balance': 0 }
cardNumber = input(" Please Enter your card Number: ")

# credit 1 
# debite 2
# print balance 3 
# exit 4 

def credit(amount=0):
    customer['balance'] = int(amount) + int(customer['balance'])
    return customer['balance']

def debit(amount=0):
    customer['balance'] = int(customer['balance']) - int(amount)
    return customer['balance']

def balances():
    return customer['balance']


operation = 0
if cardNumber == customer['card']:
    while operation != 4:
        print(f'Welcome {customer["name"]}')
        print('''
            1. Credit
            2. Debite
            3. Balance
            4.Exit''')
        operation = int(input(" Please Select your operation: "))
        if operation < 5 and operation > 0:
            if operation == 1:
                amount = int(input("Please Enter amount to be credite: "))
                balance = credit( amount)
                print(f"Current Balance : {balance}")
            elif operation == 2:
                amount = int(input('Please enter amount to be debited : '))
                balance = debit(amount)
                print(f"Current Balance : {balance}")
            elif operation == 3:
                balance = balances()
                print(f"Current Balance : {balance}")
            else:
                print('Bye')
        else:
            print('Invalid Operation ')
else:
    print('Please enter valid card number')



