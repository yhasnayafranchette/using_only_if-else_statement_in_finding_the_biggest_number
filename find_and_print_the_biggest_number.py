#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.
import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

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
        messagebox.showerror("Error", "Please enter valid numbers.")

def adjust_frame_size(event):
# Adjust frame and label sizes based on window size   
    frame_size = min(root.winfo_width(), root.winfo_height()) // 5
    frame_first_number.config(padx=frame_size, pady=frame_size)
    frame_second_number.config(padx=frame_size, pady=frame_size)
    frame_third_number.config(padx=frame_size, pady=frame_size)

root = customtkinter.CTk()
root.geometry("680x400")
root.title("Number Finder")
root.config(bg="#F9F5E7")
root.resizable(True,True)

frame_first_number = customtkinter.CTkLabel(root, text=" \n \n \n Enter the first number:", font=("Times New Roman", 24),
                                           text_color="black", bg_color="#F9F5E7", fg_color="lightblue", width=200,
                                           height=200, corner_radius=20, compound=TOP, anchor=N)
frame_first_number.grid(row=1, column=0, padx=20, pady=20, sticky=W)
entry_first_number = tk.Entry(frame_first_number)
entry_first_number.grid(row=1, column=0, padx=20, pady=20, sticky=W+E)

frame_second_number = customtkinter.CTkLabel(root, text=" \n \n \n Enter the second number:",
                                            font=("Times New Roman", 24), text_color="black", bg_color="#F9F5E7",
                                            fg_color="lightpink", width=200, height=200, corner_radius=20, compound=TOP,
                                            anchor=N)
frame_second_number.grid(row=1, column=1, padx=20, pady=20, sticky=W)
entry_second_number = tk.Entry(frame_second_number)
entry_second_number.grid(row=1, column=1, padx=20, pady=20, sticky=W+E)

frame_third_number = customtkinter.CTkLabel(root, text=" \n \n \n Enter the third number:", font=("Times New Roman", 24),
                                           text_color="black", bg_color="#F9F5E7", fg_color="lightgreen", width=200,
                                           height=200, corner_radius=20, compound=TOP, anchor=N)
frame_third_number.grid(row=1, column=2, padx=20, pady=20, sticky=W)
entry_third_number = tk.Entry(frame_third_number)
entry_third_number.grid(row=1, column=2, padx=20, pady=20, sticky=W+E)   

number_finder_button = tk.Button(root, text="Find Biggest Number", command=find_and_print_biggest_number)
number_finder_button.grid(row=2, column=0, columnspan=3, pady=10)

biggest_number_label = tk.Label(root, text="", font=("Times New Roman", 16), foreground="green")
biggest_number_label.grid(row=3, column=0, columnspan=3, pady=10)

# Bind the resize function to the Configure event of the root window
root.bind("<Configure>", adjust_frame_size)

# Run the Tkinter event loop
root.mainloop()
