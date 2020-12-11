import tkinter


def convert_clicked():
    miles = float(mile_entry.get())
    km_conv = 1.60934 * miles
    converted_label.config(text=round(km_conv, 2))


window = tkinter.Tk()
window.minsize(width=200, height=100)
window.title('Mile to Km Converter')
window.config(padx=5, pady=5)

mile_entry = tkinter.Entry(width=10)
mile_entry.grid(column=1, row=0)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

convert_button = tkinter.Button(text="Calculate", command=convert_clicked)
convert_button.grid(column=1, row=2)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_label = tkinter.Label(text=0)
converted_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
