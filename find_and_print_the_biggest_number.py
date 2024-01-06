#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.
import customtkinter
import tkinter as tk
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
root.geometry("1000x365")
root.title("Number Finder")
root.config(bg="#F9F5E7")
root.resizable(False,False)

frame_first_number = tk.Frame(root, bg="lightblue", padx=20, pady=20)
frame_first_number.grid(row=1, column=0, padx=10, pady=10)

frame_second_number = tk.Frame(root, bg="lightpink", padx=20, pady=20)
frame_second_number.grid(row=1, column=1, padx=10, pady=10)

frame_third_number = tk.Frame(root, bg="lightgreen", padx=20, pady=20)
frame_third_number.grid(row=1, column=2, padx=10, pady=10)

first_number_label = tk.Label(frame_first_number, text="Enter the first number:", font=("Times New Roman", 12), bg="lightblue", fg="black")
first_number_label.grid(row=0, column=0, padx=10, pady=10)
entry_first_number = tk.Entry(frame_first_number)
entry_first_number.grid(row=1, column=0, padx=10, pady=10)

second_number_label = tk.Label(frame_second_number, text="Enter the second number:", font=("Times New Roman", 12), bg="lightpink", fg="black")
second_number_label.grid(row=0, column=0, padx=10, pady=10)
entry_second_number = tk.Entry(frame_second_number)
entry_second_number.grid(row=1, column=0, padx=10, pady=10)

third_number_label = tk.Label(frame_third_number, text="Enter the third number:", font=("Times New Roman", 12), bg="lightgreen", fg="black")
third_number_label.grid(row=0, column=0, padx=10, pady=10)
entry_third_number = tk.Entry(frame_third_number)
entry_third_number.grid(row=1, column=0, padx=10, pady=10)    

number_finder_button = tk.Button(root, text="Find Biggest Number", command=find_and_print_biggest_number)
number_finder_button.grid(row=2, column=0, columnspan=3, pady=10)

biggest_number_label = tk.Label(root, text="", font=("Times New Roman", 16), foreground="green")
biggest_number_label.grid(row=3, column=0, columnspan=3, pady=10)

# Bind the resize function to the Configure event of the root window
root.bind("<Configure>", adjust_frame_size)

# Run the Tkinter event loop
root.mainloop()
