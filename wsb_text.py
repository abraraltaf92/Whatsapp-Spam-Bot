import tkinter as tk
from tkinter import messagebox
import webbrowser as wb
import time
import pyautogui
import pyttsx3
def run():
    try:
        if ent2.get() != int(ent2.get()) and ent3.get() != int(ent3.get()):
            pass
    except:
        tk.messagebox.showerror(title="FAILED",message="\t\t Oops! \n You have entered wrong value. Numbers can't be text values!!! ")
       
    txt = ent1.get().split()
    num = int(ent2.get())
    rep = int(ent3.get())
    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    
    tk.messagebox.showinfo(title="SUCCESS",message=f"\t\tCongratulations!\n\n You have sent {rep} times the same text to {num}")

    wb.open_new("https://wa.me/91{}".format(num))
    time.sleep(6)
    pyautogui.press("enter")
    time.sleep(12)
    for i in range(rep):
        for j in range(len(txt)):
            pyautogui.write(txt[j],interval=0.2)
            pyautogui.press("enter")

    

engine = pyttsx3.init()
engine.say("Welcome to Abrar's Whatsapp Spam Bot")
engine.runAndWait()

window = tk.Tk()
window.title("Whatsapp Spam Bot by Abrar")
window.geometry("400x400")
window.configure(bg="#3faae8")

tk.Label(window,text="Welcome",font=("Gill Sans",20),bg="green").pack(pady=10)
tk.Label(window,text="Type the text :- ",font=("Gill Sans",20)).pack(pady=20)
ent1 = tk.Entry(window)
ent1.place(x=10,y=120,height=100,width=360)

tk.Label(window,text="Enter Number :- ",font=("Gill Sans",20)).place(x=20,y=240) 
ent2 = tk.Entry(window)
ent2.place(x=180,y=240)

tk.Label(window,text="Repitition :- ",font=("Gill Sans",20)).place(x=20,y=280) 
ent3 = tk.Entry(window)
ent3.place(x=180,y=280)

button1 = tk.Button(window,text="SUBMIT",font=("Gill Sans",20),command=run)
button1.place(x=145,y=340)  # pack issue

window.mainloop()

