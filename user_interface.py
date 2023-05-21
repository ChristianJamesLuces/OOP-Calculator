
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
        operation = input("\033[92;1m" + "Choose one symbol to perform the math operation: " + "\033[0m")
        return operation
#Ask the user the operation
#Ask the user the first number
#Ask the user the second number
#Display the result
#Ask if they want to retry it
#Display 'Thank you!'