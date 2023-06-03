#Import necessary modules
from user_interface import UserInterface
import tkinter as tk
from PIL import Image, ImageTk

#Interface Update class
class InterfaceUpdate(UserInterface):
    #Define the 'thank you'
    def thank_you(self):
        window = tk.Tk()

        font = ("Arial", 18, "bold")

        text_color = "white"
        label = tk.Label(window, text="Thank you!", font=font, fg=text_color, bg = "black")
        label.pack()

        window.geometry("200x100")
        window.configure(background="black")

        window.mainloop()