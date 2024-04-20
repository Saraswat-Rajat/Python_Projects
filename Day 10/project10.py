# """this is a way of writing multi line strings, called docstrings"""

# CALCULATOR

print("CALCULATOR")


def add(n, m):
    return n + m


def sub(n, m):
    return n - m


def mult(n, m):
    return n * m


def div(n, m):
    return n / m


def pow(n, m):
    return n ** m


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "**": pow

}


def calculator():
    n = float(input("what's the first number : "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        opn_symbol = input("pick an operation: ")
        m = float(input("what's the second number : "))
        calculation_function = operations[opn_symbol]
        answer = calculation_function(n, m)
        print(f"{n} {opn_symbol} {m} = {answer}")

        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation :  ") == "y":
            n = answer
        else:
            should_continue = False
            calculator()


calculator()
