from tkinter import *


def calculator():
    miles = float(entry.get())
    km = round(miles * 1.609344)
    label_3.config(text=f"{km}")


window = Tk()
window.title("Mil to Km Converter")
window.config(padx=20, pady=20)

# Text box
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Labels
label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)
label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)
label_3 = Label(text="0")
label_3.grid(row=1, column=1)
label_4 = Label(text="Km")
label_4.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=calculator)
button.grid(row=2, column=1)

window.mainloop()
