from curses import window
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label= tkinter.Label(text = " This is a label ", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

def button_click():
    print("Clicked")
    my_label["text"]= input.get()

button = tkinter.Button(text="Click here!", command=button_click)
button.pack()

input = tkinter.Entry(width=10)
input.pack()

window.mainloop()