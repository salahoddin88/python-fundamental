customer = [{'name' : 'Nikhil', 'card':'123456', 'balance': 0 }, {'name' : 'Abhishek', 'card':'987654', 'balance': 0 }]
cardNumber = input(" Please Enter your card Number: ")

# credit 1 
# debite 2
# print balance 3 
# exit 4 

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
                balance = int(input("Please Enter amount to be credite: "))
                customer['balance'] = customer['balance'] + balance
                print(f"Current Balance : {customer['balance']}")
            elif operation == 2:
                balance = int(input('Please enter amount to be debited : '))
                if customer['balance']  == 0:
                    print("Your current balance is 0")
                elif customer['balance'] < balance:
                    print(f"Your current balance is {customer['balance']}")
                else:
                    customer['balance'] = customer['balance'] - balance
                    print(f"Current Balance : {customer['balance']}")
            elif operation == 3:
                print(f"Current Balance : {customer['balance']}")
            else:
                print('Bye')
        else:
            print('Invalid Operation ')
else:
    print('Please enter valid card number')



