#Importing the necessary modules
from tkinter import simpledialog, messagebox

#Define User interface class
class UserInterface:
    #Display the welcome message and its function
    def intro(self):
        messagebox.showinfo("Welcome", "Welcome to the Simple Calculator App!")

    #Display the operations
    def operations(self):
        valid_operators = ['+', '-', '/', '*', "**"]
        while True:
            operation = simpledialog.askstring("Choose Operation", "Choose one symbol to perform the math operation (+, -, *, /, **): ")
            if operation in valid_operators:
                return operation
            elif operation is None:
                return None
            else:
                messagebox.showerror("Invalid Operator", "Please choose a valid operator.")

    
    #Ask the user for the numbers
    def get_numbers(self):
        while True:
            try:
                number1 = simpledialog.askfloat("Input Number", "Input your first number: ")
                number2 = simpledialog.askfloat("Input Number", "Input your second number: ")
                return number1, number2
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a number")

    #Display the result
    def display_result(self, result):
        messagebox.showinfo("Result", "Result: " + str(result))
    #Ask if they want to retry it
    def ask_try_again(self):
        response = messagebox.askyesno("Try Again", "Do you want to try again?")
        return response

    #Display 'Thank you!'
    def thank_you(self):
        messagebox.showinfo("(:SLAYYYYY:)", "Thank you!")