from tkinter import *

root = Tk()
root.geometry("300x400")
# root.configure(bg="white")
root.title('Demo')

def calculate():
	print(eval(field.get()))


lbl = Label(root, text='Assistant', font=('Arial Bold', 20)).pack()

field = Entry(root)
field.pack(pady=20)

btn = Button(root, text='Search', command=calculate).pack(pady=20)
root.mainloop()