import tkinter as tk
from tkinter import ttk

def button_func():
    print('ooi')

# Window
window = tk.Tk()
window.title('TKInter Variables')

# TKInter Variable
string_var = tk.StringVar()

# Widgets
label = ttk.Label(master=window, text = 'label', textvariable=string_var)
label.pack()
entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func())
button.pack()

# Run
window.mainloop()