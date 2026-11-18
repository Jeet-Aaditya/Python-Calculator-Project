print('BASIC CALCULATOR')
print('Enter two numbers and an operator (+, -, *, /) to calculate the result.')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operator = input('Enter an operator (+, -, *, /): ')

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: Division by zero!'


if operator == '+':
    print('Result:', addition(num1, num2))
elif operator == '-':
    print('Result:', subtraction(num1, num2))
elif operator == '*':
    print('Result:', multiplication(num1, num2))
elif operator == '/':
    print('Result:', division(num1, num2))
else:
    print('Invalid operator!')
    

