import tkinter as tk
import customtkinter as ctk
import runpy
import os
import configuration
import time



# Initialize the main application window
initapp = ctk.CTk()
initapp.focus_force()
initapp.geometry("300x400+200+200")
initapp.title("Initial")

playernol = ctk.CTkLabel(master=initapp, text="Number of Players")
playernol2 = ctk.CTkLabel(master=initapp, text="(not including dealer)")
playernol.pack(anchor=ctk.N, pady=0)
playernol2.pack(anchor=ctk.N, pady=0)
players = tk.Spinbox(master=initapp, from_=1, to=3, width=5, state='readonly')
players.pack(anchor=ctk.N, pady=5)
yourposl = ctk.CTkLabel(master=initapp, text="Your Position")
yourposl.pack(anchor=ctk.N, pady=5)
yourpos = tk.Spinbox(master=initapp, from_=1, to=3, width=5, state='readonly')
yourpos.pack(anchor=ctk.N, pady=5)




# cerate and place the label for the number of decks
dislabel = ctk.CTkLabel(master=initapp, text="Number of Decks in Shoe")
dislabel.pack(anchor=ctk.N, pady=5)

# make the spinbox to select the number of decks
dis = tk.Spinbox(master=initapp, from_=1, to=8, width=5, state='readonly')
dis.pack(anchor=ctk.N, pady=5)

over18 = ctk.CTkCheckBox(master=initapp, text="I am over 18")
over18.pack(anchor=ctk.N, pady=5)

#Fstart of cards
def calculate_distribution():
    if not over18.get():
        print("You must be over 18 to play.")
        over18error = ctk.CTkLabel(master=initapp, text="You must be over 18 to play.",text_color='red',font=("Menlo", 12))
        over18error.pack(anchor=ctk.N)
        return
    decks = int(dis.get())
    configuration.decks = decks
    current_dis = {}
    cards = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes', 'sevens', 'eights', 'nines', 'tvcs']
    for card in cards:
        configuration.current_decks[card] = current_dis[card] = decks * 4
        configuration.current_decks['tvcs'] = current_dis['tvcs'] = decks * 16
        configuration.current_nop = int(players.get())
        configuration.playerpos = int(yourpos.get())
    current_players = int(players.get())
    current_pos = int(yourpos.get())
    if current_pos > current_players:
        print("Invalid position")
        invpos = ctk.CTkLabel(master=initapp, text="Invalid Position.",text_color='red',font=("Menlo", 12))
        invpos2 = ctk.CTkLabel(master=initapp, text="Postion must be less than № of players.",text_color='red',font=("Menlo", 12))
        invpos.pack(anchor=ctk.N)
        invpos2.pack(anchor=ctk.N)
        return

    else:
        print(configuration.current_decks)
        print(current_players)
        initapp.destroy()
        runpy.run_path(os.path.join(configuration.current_dir, 'game.py'))


    


# Button to trigger the game
begin = ctk.CTkButton(master=initapp, text="Begin", command=calculate_distribution)
begin.pack(anchor=ctk.N, pady=10)

# Button to exit the application
end = ctk.CTkButton(master=initapp, command=initapp.destroy, text="Exit")
end.pack(anchor=ctk.S, pady=10)

# Start the application's main event loop
initapp.mainloop()

print("init")
