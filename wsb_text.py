import tkinter as tk
import webbrowser as wb
import time
import pyautogui
import pyttsx3
def run():

    txt = ent1.get().split()
    num = int(ent2.get())
    rep = int(ent3.get())
    

    wb.open_new("https://wa.me/91{}".format(num))
    time.sleep(10)
    pyautogui.press("enter")
    time.sleep(15)
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
import os 
os.getcwd()

