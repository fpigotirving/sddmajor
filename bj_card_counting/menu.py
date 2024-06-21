import tkinter as tk
import customtkinter as ctk
import os
# import config
import sys
import time
import runpy
from tkinter import messagebox
from tkinter import filedialog
import configuration
from PIL import Image

ctk.set_default_color_theme("green")


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = ctk.CTk()
app.focus_force()
app.geometry("300x400+200+200")
app.title("Menu")
def test_button():
        print("function called")


title = ctk.CTkLabel(master=app, text="Blackjack Card Counting Application", font=("Menlo", 12))
title.pack(anchor=ctk.N,pady=10)
def init():
    app.destroy()
    runpy.run_path(os.path.join(configuration.current_dir, 'init2.py'))
    
ng = ctk.CTkButton(master=app, command=init, text="New Game")
ng.pack(anchor=ctk.N,pady=10)
load = ctk.CTkButton(master=app, command=lambda: runpy.run_path(os.path.join(configuration.current_dir, 'lg.py')), text="Load Game")
load.pack(anchor=ctk.N,pady=10)

options = ctk.CTkButton(master=app, command=lambda: runpy.run_path(os.path.join(configuration.current_dir, 'settings.py')), text="Options")
options.pack(anchor=ctk.N,pady=10)



end = ctk.CTkButton(master=app, command=app.destroy, text="Exit")
end.pack(anchor=ctk.S,pady=10)
'''button = ctk.CTkButton(master=app, command=test_button, text="Click Me")
button.pack(anchor=ctk.N)'''
gr = ctk.CTkLabel(master=app, text="© 2024. Gamble responsibly.",font=("Menlo", 12))
gr.pack(anchor=ctk.S,pady=5)
dis1 = ctk.CTkLabel(master=app, text="Disclaimer: Card Counting is frowned upon in most casinos.",font=("Menlo", 8))
dis2 = ctk.CTkLabel(master=app, text="This application is intended for educational purposes only.",font=("Menlo", 8)) 
dis1.pack(anchor=ctk.S,pady=0)
dis2.pack(anchor=ctk.S,pady=0)
app.mainloop()

