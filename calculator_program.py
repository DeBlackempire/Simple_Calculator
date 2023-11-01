# Importing Tkinter
from tkinter import *

# Create a root window
root = Tk()
root.title("Calculator")

# Create a StringVar object to store the input and output
input_output = StringVar()

# Create an Entry widget to display the input and output
entry = Entry(root, textvariable=input_output, font=("Arial", 20), justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create a Frame widget to hold the buttons
frame = Frame(root)
frame.grid(row=1, column=0, padx=5, pady=5)


# Define functions to handle the button clicks and perform the calculations
def click(number):
    # Append the number to the input
    input_output.set(input_output.get() + str(number))


def clear():
    # Clear the input and output
    input_output.set("")


def equal():
    # Evaluate the input and display the output
    try:
        output = str(eval(input_output.get()))
        input_output.set(output)
    except:
        input_output.set("Error")


# Create Button widgets for each digit, operator, decimal point, equal sign and clear function
button_1 = Button(frame, text="1", width=5, height=2, command=lambda: click(1))
button_2 = Button(frame, text="2", width=5, height=2, command=lambda: click(2))
button_3 = Button(frame, text="3", width=5, height=2, command=lambda: click(3))
button_4 = Button(frame, text="4", width=5, height=2, command=lambda: click(4))
button_5 = Button(frame, text="5", width=5, height=2, command=lambda: click(5))
button_6 = Button(frame, text="6", width=5, height=2, command=lambda: click(6))
button_7 = Button(frame, text="7", width=5, height=2, command=lambda: click(7))
button_8 = Button(frame, text="8", width=5, height=2, command=lambda: click(8))
button_9 = Button(frame, text="9", width=5, height=2, command=lambda: click(9))
button_0 = Button(frame, text="0", width=11, height=2, command=lambda: click(0))
button_plus = Button(frame, text="+", width=5, height=2, command=lambda: click("+"))
button_minus = Button(frame, text="-", width=5, height=2, command=lambda: click("-"))
button_multiply = Button(frame, text="*", width=5, height=2,
                         command=lambda: click("*"))
button_divide = Button(frame,
                       text="/",
                       width=5,
                       height=2,
                       command=lambda: click("/"))
button_point = Button(frame,
                      text=".",
                      width=5,
                      height=2,
                      command=lambda: click("."))
button_equal = Button(frame,
                      text="=",
                      width=5,
                      height=6,
                      command=lambda: equal())
button_clear = Button(frame,
                      text="C",
                      width=11,
                      height=2,
                      command=lambda: clear())

# Use the grid method to arrange the buttons in a grid layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=2)
button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_point.grid(row=4, column=2)
button_equal.grid(row=5, column=3, rowspan=2)
button_clear.grid(row=5, column=0, columnspan=2)

# Use the mainloop method to run the app
root.mainloop()
