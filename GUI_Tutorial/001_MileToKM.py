import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


# Window
window = ttk.Window(themename='journal')
window.title('Demo')

# Set Width & Height
window.geometry('300x150')

# Title
title_label = ttk.Label(
    master=window, text='Miles to Kilometers', font='Calibri 24 bold')
title_label.pack(pady=10)

# Input Field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side='left', padx=10)
button.pack()
input_frame.pack()

# Output Label
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output",
                         font='bold 16', textvariable=output_string)
output_label.pack(pady=10)

# Run
window.mainloop()
