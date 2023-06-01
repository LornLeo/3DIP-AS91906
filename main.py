from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('1000x600')
window.title("Menu")
window.resizable(0, 0)
window.configure(bg="white")
lblun=Label(window,text="Our Menu ",font=('Rockwell 20'),bg='#fcc302',fg="white",width=12,padx=30,anchor=W)
lblun.grid(row=0,column=0,pady=30)





window.mainloop()
