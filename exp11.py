import tkinter as tk

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, str(current) + str(number))

def button_clear():
    entry_display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, result)
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for display
entry_display = tk.Entry(root, width=35, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Add buttons to the grid
row_num = 1
col_num = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=40, pady=20, command=button_equal).grid(row=row_num, column=col_num)
    elif button == "0":
        tk.Button(root, text=button, padx=40, pady=20, command=lambda: button_click(0)).grid(row=row_num, column=col_num)
    elif button == ".":
        tk.Button(root, text=button, padx=40, pady=20, command=lambda: button_click(".")).grid(row=row_num, column=col_num)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda num=button: button_click(num)).grid(row=row_num, column=col_num)
    
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Clear button
tk.Button(root, text="Clear", padx=85, pady=20, command=button_clear).grid(row=row_num, column=0, columnspan=4)

# Start the GUI main loop
root.mainloop()
