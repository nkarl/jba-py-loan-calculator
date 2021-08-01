"""calculator class for annuity payments."""
import math


class Annuity:
    @staticmethod
    def nominal(interest):
        """Compute the nominal (interest) rate"""
        return (interest / 100) / 12

    @staticmethod
    def option_n():
        """When the user enters 'n'; computes the numbers of months required."""
        principal = int(input("Enter the loan principal:"))
        a_monthly = int(input("Enter the monthly payment:"))
        interest = float(input("Enter the loan interest:"))

        def get_periods():
            i = Annuity.nominal(interest)
            tmp = a_monthly / (a_monthly - i * principal)
            return math.ceil(math.log(tmp, i + 1))

        periods = get_periods()
        y = periods // 12
        m = periods - (y * 12)
        print(f"It will take {y} years and {m} months to repay this loan!")

    @staticmethod
    def option_a():
        """When the user enters 'a'; computes the monthly payment."""
        principal = int(input("Enter the loan principal:"))
        periods = int(input("Enter the number of periods:"))
        interest = float(input("Enter the loan interest:"))

        def get_monthly():
            i = Annuity.nominal(interest)
            return (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)

        a_monthly = int(math.ceil(principal * get_monthly()))
        print(f"Your monthly payment = {a_monthly}!")

    @staticmethod
    def option_p():
        """When the user enters 'p'; computes the total (principal) loan."""
        a_monthly = float(input("Enter the annuity payment:"))
        periods = int(input("Enter the number of periods:"))
        interest = float(input("Enter the loan interest:"))

        def get_principal():
            i = Annuity.nominal(interest)
            temp = (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
            return a_monthly / temp

        principal = get_principal()
        print(f"Your loan principal = {principal}")

    @staticmethod
    def calculator():
        """Entry point function; asks user to select which option to compute."""
        print("What do you want to calculate?")
        print("type \"n\" for number of monthly payments,")
        print("type \"a\" for annuity monthly payment amount,")
        print("type \"p\" for loan principal:")
        option = input()

        if option == "n":
            Annuity.option_n()
        if option == "a":
            Annuity.option_a()
        if option == "p":
            Annuity.option_p()
