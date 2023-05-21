#Import the module and files
from user_interface import UserInterface
from calculator_class import Calculator

ui = UserInterface()
calcu = Calculator()

ui.intro()

while True:
    operation = ui.operations()
    number1, number2 = ui.get_numbers()
    
    try:
        result = calcu.calculate_result(number1, number2, operation)
        ui.display_result(result)
    except ZeroDivisionError as e:
        ui.display_result("Error", str(e))

    if not ui.ask_try_again():
        ui.thank_you()
        break
#Create an instance and run it