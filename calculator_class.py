#Define the Calculator class
class Calculator:
    #Define the Operators
    def __init__(self):
        self.operations = ['+', '-', '/', '*']

    #Define the Addition
    def add(self, number1, number2):
        return number1 + number2
    
    #Define the Subtraction
    def subtract(self, number1, number2):
        return number1 - number2
    
    #Define the Multiplication
    def multiply(self, number1, number2):
        return number1 * number2
    
    #Define the Division
    def divide(self, number1, number2):
        if number2 != 0:
            return number1 / number2
        else:
            raise ValueError("Invalid Input: Cannot be divide by zero.")
        
    #Calculate the result
    def calculate_result(self, number1, number2, operations):
        if operations == '+':
            return self.add(number1, number2)
        elif operations == '-':
            return self.subtract(number1, number2)
        elif operations == '*':
            return self.multiply(number1, number2)
        elif operations == '/':
            return self.divide(number1, number2)