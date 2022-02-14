from tkinter import Tk, Label, Button

root = Tk()
root.geometry("400x400")

def clicker():
    my_label = Label(root, text="You clicked a button")

my_button = Button(root, text="Click here")
my_button.bind("<Button-1>", clicker)
my_button.pack(pady=20)

button_key = Button()

root.mainloop()
