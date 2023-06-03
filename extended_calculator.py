#Import necessary modules
from calculator_class import Calculator


#Updated the Calculator class
class ExtendedCalculator(Calculator):
    #Define the exponent
    def power(self, number1, number2):
        return number1 ** number2