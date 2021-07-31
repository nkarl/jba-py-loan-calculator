"""credit calculator"""
import math


def nominal(interest):
    return (interest / 100) / 12


def option_n():
    principal = int(input("Enter the loan principal:"))
    a_monthly = int(input("Enter the monthly payment:"))
    interest = float(input("Enter the loan interest:"))

    def get_periods():
        i = nominal(interest)
        tmp = a_monthly / (a_monthly - i * principal)
        return math.ceil(math.log(tmp, i+1))
    periods = get_periods()
    y = periods // 12
    m = periods - (y * 12)
    print(f"It will take {y} years and {m} months to repay this loan!")


# When the user enter 'm'
def option_a():
    principal = int(input("Enter the loan principal:"))
    periods = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))

    def get_monthly():
        i = nominal(interest)
        return (i * (1+i) ** periods) / ((1+i) ** periods - 1)

    a_monthly = int(math.ceil(principal * get_monthly()))
    print(f"Your monthly payment = {a_monthly}!")


# When the user enter 'p'
def option_p():
    a_monthly = float(input("Enter the annuity payment:"))
    periods = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))

    def get_principal():
        i = nominal(interest)
        temp = (i * (1+i) ** periods) / ((1+i) ** periods - 1)
        return a_monthly / temp

    principal = get_principal()
    print(f"Your loan principal = {principal}")


# Entry point function
def calculator():
    print("What do you want to calculate?")
    print("type \"n\" for number of monthly payments,")
    print("type \"a\" for annuity monthly payment amount,")
    print("type \"p\" for loan principal:")
    option = input()

    if option == "n":
        option_n()
    if option == "a":
        option_a()
    if option == "p":
        option_p()
    pass


if __name__ == "__main__":
    calculator()
