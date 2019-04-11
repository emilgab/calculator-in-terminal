# Asks for the first number
while True:
    try:
        num_in_1 = int(input("Please write the first number: "))
        break
    except:
        print("Sorry, not a number")

op_in = ""
while not any([ op_in == "+",
                op_in == "-",
                op_in == "*"
                ]):
    op_in = str(input("Please write +, - or *: "))

while True:
    try:
        num_in_2 = int(input("Please write the second number: "))
        break
    except:
        print("Sorry, not a number")

def calculator(num1, op_input, num2):
    '''
    The functions takes three parameters:
    - Input number 1
    - Input operator (+, - or *)
    - Input number 2
    Returns the calculation
    '''
    if op_input == "+":
        return(num1+num2)
    if op_input == "-":
        return(num1-num2)
    if op_input == "*":
        return(num1*num2)

print("%s %s %s =" % (num_in_1, op_in, num_in_2),calculator(num_in_1, op_in, num_in_2))
