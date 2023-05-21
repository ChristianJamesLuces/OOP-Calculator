
import tkinter 
import time


#Define User interface class
class UserInterface:
    #Display the welcome message and its function
    def intro(self):
        intro = ("WELCOME")
        print("WELCOME")
        print("This program is a simple app calculator that will ask the user to a math operation and perform it.")
        input("Press the ENTER key to run the program....")
        time.sleep(2)

    #Display the operations
    def operations(self):
        print("\n Addition = + \n Subtraction = - \n Multiplication = * \n Division = /\n")
        #Ask the user the operation
        operation = [input("Choose one symbol to perform the math operation: ")]
        return operation
    
    #Ask the user for the numbers
    def get_numbers(self):
        while True:
            try:
                number1 = float(input("Input your first number: "))
                number2 =  float(input("Input your second number: "))
                print("\033[30m" + "Calculating....." + "\033[0m")
                time.sleep(1)
                return number1, number2
            except ValueError:
                print("Invalid Input: Please enter a number")

    #Display the result
    def display_result(self, result):
        print("-" * 20)
        print("Result: ", result)
        print("-Operation executed-\n")

    #Error handling
    def handling_error(self, error):
        print("Error: ", error)
        print("-Operation Failed-\n")
    
    #Ask if they want to retry it
    def ask_try_again(self):
        while True:
            try_again = str(input("Do you want to try again? (yes/no): ")).lower()
            if try_again == "yes":
                return True
            elif try_again == "no":
                return False
            else:
                print("Invalid input: Please enter only 'yes or no'.")

    #Display 'Thank you!'
    def thank_you(self):
        gratitude = "\033[102;1m" + "Thank you!" + "\033[0m"
        print("\n" + ":" * 50)
        print(gratitude.center(60))
        print(":" * 50)