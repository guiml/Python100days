from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)

def button_click():
    # print("Clicked")
    label_3["text"]= int(int(input.get())*1.6)

label_0 = Label(text="      ")
label_0.grid(column=0, row=0)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=2, row=1)

label_1 = Label(text="Miles")
label_1.grid(column=3, row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)
label_3 = Label(text="0")
label_3.grid(column=2, row=2)
label_4 = Label(text="Km")
label_4.grid(column=3, row=2)

button = Button(text="Convert", command=button_click)
button.grid(column=2, row=3)

window.mainloop()