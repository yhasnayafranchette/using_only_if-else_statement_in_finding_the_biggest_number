#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.
import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

#Input three numbers from the user
def find_and_print_biggest_number():
    try:
        first_number = float(entry_first_number.get())
        second_number = float(entry_second_number.get())
        third_number = float(entry_third_number.get())
        
#Compare the numbers using if-else statement
        if first_number >= second_number and first_number >= third_number:
            biggest_number = first_number
        elif second_number >= first_number and second_number >= third_number:
            biggest_number = second_number
        else:
            biggest_number = third_number

#Display the biggest number
        biggest_number_label.config(text=f"The biggest number is: {biggest_number}")

    except ValueError:
        messagebox.showerror("Numeric Quest Error", "Please enter valid numbers.")

# Adjust frame and label sizes based on window size   
def adjust_frame_size(event):
    frame_size = min(root.winfo_width(), root.winfo_height()) 
    frame_first_number.config(padx=frame_size, pady=frame_size)
    frame_second_number.config(padx=frame_size, pady=frame_size)
    frame_third_number.config(padx=frame_size, pady=frame_size)
 
root = customtkinter.CTk()
root.geometry("1050x530")
root.title("Numeric Quest")
root.config(bg="#F9F5E7")
root.resizable(False,False)

#Create title of the window
title_label = tk.Label(root, text="Numeric Quest: Uncover the Biggest Digit!", font=("Monotype Corsiva", 40), bg="#F9F5E7", foreground="#19376D")
title_label.grid(row=0, column=0, columnspan=3, padx=8, pady=20)

#Create frames and entry widgets for the three input numbers
frame_first_number = customtkinter.CTkLabel(root, text=" \n \n Enter the first number:", font=("Century Gothic", 20),
                                        text_color="black", bg_color="lightblue", fg_color="lightblue", width=200,
                                        height=100, compound=TOP, anchor=N)
frame_first_number.grid(row=1, column=0, padx=20, pady=20, sticky=W)
entry_first_number = tk.Entry(frame_first_number, bg="white", fg="black", bd=3, width=20, font=("Century Gothic", 18))
entry_first_number.grid(row=1, column=0, padx=20, pady=20, sticky=W+E)

frame_second_number = customtkinter.CTkLabel(root, text=" \n \n Enter the second number:",
                                            font=("Century Gothic", 20), text_color="black", bg_color="lightpink",
                                            fg_color="lightpink", width=200, height=100, compound=TOP,
                                            anchor=N)
frame_second_number.grid(row=1, column=1, padx=20, pady=20, sticky=W) 
entry_second_number = tk.Entry(frame_second_number, bg="white", fg="black", bd=3, width=20, font=("Century Gothic", 18))
entry_second_number.grid(row=1, column=0, padx=20, pady=20, sticky=W+E)  

frame_third_number = customtkinter.CTkLabel(root, text=" \n \n Enter the third number:", font=("Century Gothic", 20),
                                           text_color="black", bg_color="lightgreen", fg_color="lightgreen", width=200,
                                           height=100, compound=TOP, anchor=N)
frame_third_number.grid(row=1, column=2, padx=20, pady=20, sticky=N+S+E+W) 
entry_third_number = tk.Entry(frame_third_number, bg="white", fg="black", bd=3, width=20, font=("Century Gothic", 18))
entry_third_number.grid(row=1, column=0, padx=20, pady=20, sticky=N+S+E+W)  

# Create button to find the biggest number
number_finder_button = tk.Button(root, text="Find the Biggest Number", command=find_and_print_biggest_number, width=30, height=2, font=("Century Gothic", 16), bg="#E0AED0", fg="black")
number_finder_button.grid(row=2, column=0, columnspan=3, pady=10)

# Color change in the button if mouse pointer is on it
def on_enter(event):
    number_finder_button['background'] = '#A367B1'

def on_leave(event):
    number_finder_button['background'] = '#E0AED0'

number_finder_button.bind('<Enter>', on_enter)
number_finder_button.bind('<Leave>', on_leave)

# Create label to display the result
biggest_number_label = tk.Label(root, text="", font=("Monotype Corsiva", 40), bg="#F9F5E7", foreground="red")
biggest_number_label.grid(row=3, column=0, columnspan=3, pady=10)

# Bind the resize function to the Configure event of the root window
root.bind("<Configure>", adjust_frame_size)

# Run the Tkinter event loop
root.mainloop()
