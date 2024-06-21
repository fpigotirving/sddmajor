import tkinter as tk
import customtkinter as ctk
import runpy
import os
import configuration
from tkinter import messagebox

# intinierge
initapp = ctk.CTk()
initapp.focus_force()
initapp.geometry("300x400+200+200")
initapp.title("Load Game")

# Get the current directory
current_directory = os.getcwd()

# List to store text file names
text_files = []

# Iterate over the files in the current directory
for file in os.listdir(current_directory):
    # Check if the file is a text file
    if file.endswith(".txt"):
        if file == "savefile_syntax.txt": #omit the included savefile_syntax.txt file as this is not a save file
            continue
        text_files.append(file)




# Print the list of text file names
print(text_files)
'''if len(text_files) == 0:
    messagebox.showerror("Error", "No save files found.")
    initapp.destroy()'''

sgl = ctk.CTkLabel(master=initapp, text="Select Game")
sgl.pack(anchor=ctk.N, pady=0)

sg = ctk.CTkComboBox(master=initapp, values=text_files, state='readonly')
sg.pack(anchor=ctk.N, pady=5)



def loadgame():
    configuration.game_source = "Load"
    loading = sg.get()
    print("Loading game")
    print(loading)
    f = open(loading, "r")
    lines = f.readlines()
    print(lines)
    for line in lines:
        line.removesuffix("\n")
        print(line)
    print(lines)
    configuration.decks = int(lines[0])
    configuration.playerpos = int(lines[1])
    configuration.current_nop = int(lines[2])
    loadednop = int(lines[2])
    # blank
    # expected next card, not in use
    # shoe value, not in use
    n = 6
    for card in configuration.cards: #used to be 11 lines, made this much more efficient
        configuration.initial_counts[card] = int(lines[n])
        n += 1
    loadedplayerposf = (lines[16])
    # blank
    runpy.run_path(os.path.join(configuration.current_dir, 'game.py'))






load = ctk.CTkButton(master=initapp, command=loadgame, text="Load Game")
load.pack(side=ctk.BOTTOM, pady=10)
note = ctk.CTkLabel(master=initapp, text="Note: Saved game will start on new hand.", text_color='red')

note2 = ctk.CTkLabel(master=initapp, text="If the below button does not do anything,", text_color='red')
note3 = ctk.CTkLabel(master=initapp, text="the file you have chosen is not a valid save file.", text_color='red')
note4 = ctk.CTkLabel(master=initapp, text="Please choose a valid save file.", text_color='red')

note4.pack(side=ctk.BOTTOM, pady=0)
note3.pack(side=ctk.BOTTOM, pady=0)
note2.pack(side=ctk.BOTTOM, pady=0)
note.pack(side=ctk.BOTTOM, pady=10)

# loadeddecksused = 



initapp.mainloop()

