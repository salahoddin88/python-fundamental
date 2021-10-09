
def addition(num1, num2):
    c = num1 + num2
    return c

def substration(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    print('Division by zero is not allowed')
    

def main():
    operation = 0
    while operation != 5:
        a = int(input(' Enter Number 1: '))
        b = int(input(' Enter Number 2: '))
        print(''' 
            1. Addition
            2. Sub
            3. Mul
            4. Div
        ''')
        operation = int(input('Please Enter Operation: '))
        if operation == 1:
            add = addition(a, b)
            print(f"{a} + {b} = {add}")
        elif operation == 2:
            sub = substration(a, b)
            print(f"{a} - {b} = {sub}")
        elif operation == 3:
            mul = multiplication(a, b)
            print(f"{a} * {b} = {mul}")
        elif operation == 4:
            div = division(a, b)
            if div:
                print(f"{a} / {b} = {div}")
        else :
            print("Thank You")
            
# main()


def Args(a, b, *c):
    print('a=>', a)
    print('b=>', b)
    for arg in c:
        print(arg)

# Args('Hello', 'My Name', 'Salahuddin', 'I am ', 'Developer', 'I live', 'in Nashik')


def hello(**student):
    print(type(student))
    print(student['firstName'])
    print(student['adress'])

hello(firstName='Salahuddin', lastName="Shaikh", adress="Nashik")


