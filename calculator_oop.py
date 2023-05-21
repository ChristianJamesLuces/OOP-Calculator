#Import the module and files
from user_interface import UserInterface
from calculator_class import Calculator

#Creating the instances
ui = UserInterface()
calcu = Calculator()

ui.intro() #Display the intro

#Loop with True condition
while True:
    operation = ui.operations() #Display the operations
    number1, number2 = ui.get_numbers() #Ask the user for the numbers
    
    try:
        result = calcu.calculate_result(number1, number2, operation) 
        ui.display_result(result) #Display the result
    except ZeroDivisionError as e:
        ui.display_result("Error", str(e)) #Show the error

    if not ui.ask_try_again():
        ui.thank_you() #Display the 'Thank you!'
        break