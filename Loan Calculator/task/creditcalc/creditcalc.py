"""credit calculator"""
import math
import argparse
from annuity import Annuity

parser = argparse.ArgumentParser(
    description="This is the Differentiate Loan Payment Calculator. \
                It accepts optional CLI arguments for computation.")

parser.add_argument("--type", default="annuity", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--period", type=int)
parser.add_argument("--interest", type=float)


if __name__ == "__main__":
    Annuity.calculator()
