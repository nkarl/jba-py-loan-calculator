"""calculator class for Differentiate Loan Payments"""
import math


class Diff:
    """
    This class is used to compute values in Differentiate Loan Payments.
    """
    @staticmethod
    def nominal(interest):
        """Compute the nominal (interest) rate"""
        return (interest / 100) / 12
