import tkinter as tk
from tkinter import ttk

# Button Function


def button_func():
    print('a Button Pressed')


def exercise_button_func():
    print('Hello')


# Create Window
window = tk.Tk()
window.title('Windows and Widgets')
window.geometry('800x500')

# Create Widgets
text = tk.Text(master=window)
text.pack()

# TTK Widgets
label = ttk.Label(master=window, text='This is a text')
label.pack()

# TTK Entry
entry = ttk.Entry(master=window)
entry.pack()

# Exercise Label
textLabel = ttk.Label(master=window, text='my label')
textLabel.pack()

# TTK Button
button = ttk.Button(master=window, text='Button', command=button_func)
button.pack()

# Exercise
# Add One More Text Label, And a Button with Function that Prints 'Hello'
# The label should say "my label" and be between entry widget and the button

# buttonHello = ttk.Button(
# master=window, text='exercise button', command=exercise_button_func)
buttonHello = ttk.Button(
    master=window, text='exercise button', command=lambda: print('hello'))
buttonHello.pack()

# Run
window.mainloop()
print('Hello')
