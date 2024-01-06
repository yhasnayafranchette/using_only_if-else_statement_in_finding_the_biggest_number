#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("450x300")
root.title("Number Finder")

#Input three numbers from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

#Compare the numbers using if-else statement
if first_number >= second_number and first_number >= third_number:
    biggest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    biggest_number = second_number
else:
    biggest_number = third_number

#Print the biggest number
print("The biggest number is:", biggest_number)

root.mainloop()