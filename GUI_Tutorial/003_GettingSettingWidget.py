import tkinter as tk
from tkinter import ttk


def button_func():
    print(entry.get())


# Window
window = tk.Tk()
window.title('Getting & Setting Widgets')
window.geometry('400x400')

# Widgets
label = ttk.Label(master=window, text='Some Text')
label.pack()
entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text='Some Button', command=button_func)
button.pack()

# Run
window.mainloop()
