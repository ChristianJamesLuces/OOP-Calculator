#Define the Calculator class
class Calculator:
    #Define the Operators
    def __init___(self):
        self.operators = ['+', '-', '/', '*']

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
    def devide(self, number1, number2):
        if number2 != 0:
            return number1 / number2
        else:
            raise ValueError("Invalid Input: Cannot be divide by zero.")
#Calculate for the result