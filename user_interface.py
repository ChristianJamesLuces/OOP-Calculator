
import pyfiglet
import time


#Define User interface class
class UserInterface:
    #Display the welcome message and its function
    def intro(self):
        intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
        print(intro)
        print("\033[44;1m" + "This program is a simple app calculator that will ask the user to a math operation and perform it." + "\033[0m")
        input("Press the ENTER key to run the program....")
        time.sleep(2)

    #Display the operations
    def operations(self):
        print("\033[93;1m" + "\n Addition = + \n Subtraction = - \n Multiplication = * \n Division = /\n" + "\033[0m")
        #Ask the user the operation
        operation = input("\033[92;1m" + "Choose one symbol to perform the math operation: " + "\033[0m")
        return operation
    
    #Ask the user for the numbers
    def get_numbers(self):
        try:
            number1 = float(input("\033[36m" + "Input your first number: " + "\033[36m"))
            number2 =  float(input("\033[36m" + "Input your second number: " + "\033[36m"))
            print("\033[30m" + "Calculating....." + "\033[0m")
            time.sleep(1)
            return number1, number2
        except ValueError:
            print("\033[100m" + "Invalid Input: Please enter a number" + "\033[0m")

    #Display the result
    def display_result(self, result):
        print("-" * 20)
        print("\033[91;1m" + "Result: ", result, "\033[0m")
        print("\033[4m" + "-Operation executed-\n" + "\033[0m" )
#Ask if they want to retry it
#Display 'Thank you!'