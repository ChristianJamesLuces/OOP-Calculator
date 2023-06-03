#Import necessary modules
from calculator_class import Calculator


#Updated the Calculator class
class ExtendedCalculator(Calculator):
    #Define the exponent
    def power(self, number1, number2):
        return number1 ** number2
    
    def calculate_result(self, number1, number2, operation):
        if operation == '+':
            return self.add(number1, number2)
        elif operation == '-':
            return self.subtract(number1, number2)
        elif operation == '*':
            return self.multiply(number1, number2)
        elif operation == '/':
            return self.divide(number1, number2)
        elif operation == '**':
            return self.power(number1, number2)
        else:
            raise ValueError("Invalid Operation: Unrecognized operator")