"""credit calculator"""
import math
import argparse
from annuity import Annuity
from differentiate import Diff


def main():
    parser = argparse.ArgumentParser(
        description="This is the Differentiate Loan Payment Calculator. \
                    It accepts optional CLI arguments for computation.")

    parser.add_argument("--type", default="annuity", choices=["annuity", "diff"],
                        help="this is the type of payment options. \
                              Supply either 'annuity' for Annuity or 'diff' for Differentiate.")
    parser.add_argument("--payment", type=int,
                        help="(Annuity only) this is the monthly payment amount.")
    parser.add_argument("--principal", type=int,
                        help="this is the principal loan total.")
    parser.add_argument("--period", type=int,
                        help="this is the total number of payments.")
    parser.add_argument("--interest", type=float,
                        help="this is the agreed interest rate.")
    parser.parse_args()
    Annuity.calculator()


if __name__ == "__main__":
    main()
