
from tkinter import *

window = Tk()
window.title("Світло")
window.geometry("400x200")
window.configure(bg="black")

def switch_to_day(event):
    window.configure(bg="white")
    night_label.pack_forget()
    day_label.pack(expand=True)

def switch_to_night(event):
    window.configure(bg="black")
    day_label.pack_forget()
    night_label.pack(expand=True)


night_label = Label(window, text="Ніч", bg="gray", fg="black", font=("Arial", 20, "bold"), width=10, height=2)
night_label.pack(expand=True)
night_label.bind("<Button-1>", switch_to_day)


day_label = Label( window, text="День", bg="gray", fg="black", font=("Arial", 20, "bold"), width=10,  height=2)
day_label.bind("<Button-1>", switch_to_night)

window.mainloop()