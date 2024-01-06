#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("450x300")
root.title("Number Finder")

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

# Create entry labels and widgets
first_number = tk.Label(root, text="Enter the first number:", font=("Times New Roman", 12))
first_number.grid(row=0, column=0, padx=10, pady=10)
entry_first_number = tk.Entry(root)
entry_first_number.grid(row=0, column=1, padx=10, pady=10)


# Create button to find the biggest number
        
# Create label to display the result
  
# Run the Tkinter event loop
root.mainloop()
