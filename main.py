from art import logo
print(logo)



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    program_run = True
    num1 = float(input("What is your first number?: "))

    while program_run:
        print("+\n-\n*\n/")
        op = input("Pick an operation:")
        num2 = float(input("What's the next number?: "))

        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")

        question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if question == "y":
            num1 = result
        else:
            program_run = False
            print("\n" * 20)
            calculator()

calculator()