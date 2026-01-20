from tkinter import *


window = Tk()
window.title("Вікно випробувань")
window.geometry("400x400")


bt = Button(text='Суперкнопка', width=25, bg='blue', fg='white')


bt.pack(pady=20)


window.mainloop()