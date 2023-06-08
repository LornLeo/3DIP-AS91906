from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('1000x600')
window.title("Menu")
window.resizable(0, 0)
window.configure(bg="white")
left_frame=Frame(window).pack(side="left")
menu_title=Label(left_frame,text="Our Menu ",font=('Rockwell 20'),bg='#fcc302',fg="white",width=11,padx=30,pady=3,justify="left")
menu_title.pack(padx=0,anchor=NW)

window.mainloop()
