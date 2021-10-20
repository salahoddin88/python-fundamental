
class Customer:
    customers = [{'name':'Ashrith', 'card':'123', 'balance':0}, {'name':'Mukund', 'card':'456', 'balance':0}]
   
    def FetchCustomer(self, card):
        """ Fetch single Customer """
        for customer in self.customers:
            if customer['card'] == card:
                return customer
        return False
    
    def Register(self, name, card):
        """ Register New Customer """
        fetchCustomer = self.FetchCustomer(card)
        if fetchCustomer == False:
            customerData = {
                'name' : name, 
                'card' : card,
                'balance' : 0
            }
            self.customers.append(customerData)
            return customerData
        return False

    def FetchAllCustomer(self):
        """ Print All Customers List """

        for customer in self.customers:
            print(f"{customer['name']} - {customer['balance']}")

    def UpdateBalance(self, card, amount):
        """ Customers balance update (CREDIT AND DEBIT with actual values) """
        for key, customer in enumerate(self.customers):
            if card == customer['card']:
                self.customers[key]['balance'] = amount
                return customer
        return False


class ATM(Customer):
    """ ATM class which has base class Customer """

    def __init__(self, card):
        """ Making card as a global scope so we don't need to provide card for individual methods """
        self.card = card

    def Credit(self, amount):
        customer = super().FetchCustomer(self.card)
        amount = int(customer['balance']) + int(amount)
        return super().UpdateBalance(self.card, amount)

    def Debit(self, amount):
        customer = super().FetchCustomer(self.card)
        amount = int(customer['balance']) - int(amount)
        return super().UpdateBalance(self.card, amount)

    def Balance(self):
        customer = super().FetchCustomer(self.card)
        return customer



# customer = Customer()
# # customer.FetchCustomer('123')
# customer.Register('Sanket', '789')
# customer.UpdateBalance('789', 120)
# print(customer.customers)

# atm = ATM('123')
# atm.Credit(500)
# atm.Debit(200)
# atm.Balance()




def main():
    operation = 0
    while operation != 9:
        subOperation = 0
        print(''' 
        1. Transactions
        2. Register Customer
        3. Print All Customer
        9. Exit
        ''')

        operation = int(input('Select Operation: '))
        if operation == 3:
            customerObject = Customer()
            customerObject.FetchAllCustomer()
        
        elif operation == 2:
            name = input('Enter Name')
            card = input('Enter Card')
            customerObject = Customer()
            customerObject.Register(name, card)
        
        elif operation == 1:
            cardNumber = input('Enter Customers Card: ')
            ATMObject = ATM(cardNumber)
            customer = ATMObject.FetchCustomer(cardNumber)

            if customer:
                while subOperation != 9:
                    print(f'Welcom {customer["name"]}')
                    print('''
                    1. Credit
                    2. Debit
                    3. Balance
                    9. Back
                    ''')
                    subOperation = int(input('Select Operation: '))

                    if subOperation == 1:
                        amount = int(input("Enter Amount to be Credited: "))
                        customer = ATMObject.Credit(amount)
                        print(f'Current Balance is {customer["balance"]}')
                    
                    if subOperation == 2:
                        amount = int(input("Enter Amount to be Debited: "))
                        customer = ATMObject.Debit(amount)
                        print(f'Current Balance is {customer["balance"]}')
                    
                    if subOperation == 3:
                        customer = ATMObject.Balance()
                        print(f'current Balance is {customer["balance"]}')

            else:
                print('Invalid Customer')
main()