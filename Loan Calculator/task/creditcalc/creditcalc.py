"""credit calculator"""


def option_m(principal):
    print("Enter the monthly payment:")
    monthly = int(input())

    match monthly:
        case monthly if monthly == principal:
            print(f"It will take 1 month to repay the loan")
        case _:
            months = -(-principal // monthly)
            print(f"It will take {months} months to repay the loan")
    pass


def option_p(principal):
    print("Enter the number of months:")
    months = int(input())

    monthly = -(-principal // months)
    match months:
        case months if months % 2 == 0:
            print(f"Your monthly payment = {monthly}")
        case _:
            last = principal - (months - 1) * monthly
            print(f"Your monthly payment = {monthly} and the last payment = {last}")
    pass


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
