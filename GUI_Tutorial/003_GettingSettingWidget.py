import tkinter as tk
from tkinter import ttk


def button_func():

    # print(entry.get())
    # Get content of entry 
    entry_text = entry.get()

    # Update Labelhow to install tkinter
    # label.configure(text = 'some other text')
    label['text'] = entry_text

    # After we press the button, it will be disabled as the state will be disabled
    entry['state'] = 'disabled'

    # To find out the option to configure a widget
    print(label.configure())

def buttonEnableTop():
    entry['state'] = 'enabled'
    label['text'] = 'Some Text -> Enable'


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

# Exercise
# Add another button that changes text back to 'some text' and that enables entry
buttonExercse = ttk.Button(master=window, text='exercise button', command=buttonEnableTop)
buttonExercse.pack()

# Run
window.mainloop()
