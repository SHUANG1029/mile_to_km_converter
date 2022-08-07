from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)


def calculating():
    km = round(1.609344 * float(entry.get()), 2)
    label_cal.config(text=km)


entry = Entry(width=8)
entry.grid(column=1, row=0)

label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_cal = Label(text="0")
label_cal.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculating)
button.grid(column=1, row=2)

window.mainloop()
