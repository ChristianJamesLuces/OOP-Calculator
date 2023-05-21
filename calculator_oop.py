#Import the module and files
from user_interface import UserInterface
from calculator_class import Calculator

ui = UserInterface()
calcu = Calculator()

ui.intro()
operation = ui.operations()
number1, number2 = ui.get_numbers()
result = calcu.calculate_result(number1, number2, operation)
ui.display_result(result)
ui.ask_try_again()
#Create an instance and run it