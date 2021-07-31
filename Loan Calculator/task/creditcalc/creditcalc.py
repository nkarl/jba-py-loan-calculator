"""credit calculator"""


# When the user enter 'm'
def option_m(principal):
    print("Enter the monthly payment:")
    monthly = int(input())

    match monthly:
        case monthly if monthly == principal:
            print(f"It will take 1 month to repay the loan")
        case _:
            periods = -(-principal // monthly)
            print(f"It will take {periods} months to repay the loan")
    pass


# When the user enter 'p'
def option_p(principal):
    print("Enter the number of periods:")
    periods = int(input())

    monthly = -(-principal // periods)
    match periods:
        case periods if periods % 2 == 0:
            print(f"Your monthly payment = {monthly}")
        case _:
            last = principal - (periods - 1) * monthly
            print(f"Your monthly payment = {monthly} and the last payment = {last}")
    pass


# Entry point function
def calculator():
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("What do you want to calculate?")
    print("type \"m\" - for number of monthly payments,")
    print("type \"p\" - for the monthly payment:")
    option = input()

    match option:
        case "m":
            option_m(loan_principal)
        case "p":
            option_p(loan_principal)
    pass


if __name__ == "__main__":
    calculator()
