import tkinter as tk
from tkinter import messagebox, simpledialog
def add():
    try:
        
        num1 = float(entry1.get())
        entry1.config(font=("Arial", 24))
        # Password protection for history
        if not hasattr(root, "authenticated"):
            password = tk.simpledialog.askstring("Password", "Enter password:", show='*')
            if password != "hello":
                messagebox.showerror("Authentication Failed", "Incorrect password.")
                return
            root.authenticated = True
        # Add to history
        if not hasattr(root, "history"):
            root.history = []
        root.history.append(f"{num1} + {entry2.get()} = {num1 + float(entry2.get())}")
        entry2.config(font=("Arial", 24))
        num2 = float(entry2.get())
        result = num1 + num2
        result_var.set(f"{result:,}")
        result_entry.config(font=("Arial", 24))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        result = float(entry1.get()) / float(entry2.get())
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)

result_var = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
result_entry = tk.Entry(root, textvariable=result_var, state='readonly')
result_entry.grid(row=4, column=1)

root.mainloop()