import art
print(art.logo)
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
cal_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
keep_going = True
previous_result = 0
first_number = float(input("Type the first number: \n"))
while keep_going:
    operator = input("Choose what operation to perform\n+\n-\n*\n/\n")
    second_number = float(input("Type the second number: \n"))
    if previous_result != 0:
        previous_result = result = cal_operators[operator](previous_result, second_number)
        print(f'The result of your operation is {result}')
    else:
        previous_result = result = cal_operators[operator](first_number, second_number)
        print(f'The result of your operation is {result}')
    go_on = input("Do you want to continue working with the previous result? 'yes' 'no' ").lower()
    if go_on == 'no':
        keep_going = False
