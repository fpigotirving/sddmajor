import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import os
import configuration

print("game started")

gameappapp = ctk.CTk()
gameappapp.focus_force()
gameappapp.geometry("900x600")
gameappapp.title("Blackjack Card Counter")
gameappapp.configure(fg_color='gray20')

fontinuse = configuration.selected_font

    


players = []

if configuration.current_nop == 1:
    players = ['dealer', 'player1']
elif configuration.current_nop == 2:
    players = ['dealer', 'player1', 'player2']
elif configuration.current_nop == 3:
    players = ['dealer', 'player1', 'player2', 'player3']
else:
    print("Invalid number of players error")
    gameappapp.destroy()

labels = {}
addcard = {}
playercards = {}
current_cards = {player: [] for player in players}
current_value = {player: 0 for player in players}
holding_ace = {player: int(0) for player in players}


dmcs = ctk.CTkLabel(master=gameappapp, text="Do not worry about the dealer's concealed card.",font=(fontinuse, 12))
dmcs2 = ctk.CTkLabel(master=gameappapp, text="It will be automatically accounted for.",font=(fontinuse, 12))
dmcs.place(anchor='n', relx=0.2, rely=0.025)
dmcs2.place(anchor='n', relx=0.2, rely=0.075)



cardsf = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card_internal = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'tvcs'] #ten valued cards
cardpics = ["🃁", "🃂", "🃃", "🃄", "🃅", "🃆", "🃇", "🃈", "🃉", "🃊", "🃋", "🃍", "🃎"]
dealermysterycard = True
cards_in_shoe = {card: 4*configuration.decks for card in card_internal}
cards_in_shoe['tvcs'] = 16*configuration.decks
print(cards_in_shoe)
expected_next_card = str()
shoe_value = 0
    
card_mapping = dict(zip(cardsf, cardpics))

if configuration.game_source == "Load": #loading save
    print("Loading game")
    cards_in_shoe['Ace'] = int(configuration.initial_counts['aces'])
    cards_in_shoe['2'] = int(configuration.initial_counts['twos'])
    cards_in_shoe['3'] = int(configuration.initial_counts['threes'])
    cards_in_shoe['4'] = int(configuration.initial_counts['fours'])
    cards_in_shoe['5'] = int(configuration.initial_counts['fives'])
    cards_in_shoe['6'] = int(configuration.initial_counts['sixes'])
    cards_in_shoe['7'] = int(configuration.initial_counts['sevens'])
    cards_in_shoe['8'] = int(configuration.initial_counts['eights'])
    cards_in_shoe['9'] = int(configuration.initial_counts['nines'])
    cards_in_shoe['tvcs'] = int(configuration.initial_counts['tvcs'])
    print(cards_in_shoe)
    current_cards['dealer'] = configuration.loadeddealercards
    current_cards['player1'] = configuration.loadedplayer1cards
    current_value['dealer'] = configuration.loadeddealerhandvalue
    current_value['player1'] = configuration.loadedplayer1handvalue
    holding_ace['dealer'] = configuration.loadeddealeraces
    holding_ace['player1'] = configuration.loadedplayer1aces
    if configuration.current_nop >= 2:
        current_cards['player2'] = configuration.loadedplayer2cards
        current_value['player2'] = configuration.loadedplayer2hv
        holding_ace['player2'] = configuration.loadedplayer2aces
    if configuration.current_nop == 3:
        current_cards['player3'] = configuration.loadedplayer3cards
        current_value['player3'] = configuration.loadedplayer3hv
        holding_ace['player3'] = configuration.loadedplayer3aces
    print("Game loaded")


#Calculate the total value of the shoe in order to determine the most likely next card.
def calculate_shoe_value(): #custom algorithm
    global shoe_value
    shoe_value = 0
    for card in cards_in_shoe:
        if card in ['2', '3', '4', '5', '6', '7', '8', '9']:
            shoe_value += (int(card) * cards_in_shoe[card])
        elif card == 'tvcs':
            shoe_value += (10 * cards_in_shoe['tvcs'])
        elif card == 'Ace':
            shoe_value += (11 * cards_in_shoe['Ace'])
        print("success for", card)
    print("Shoe value:", shoe_value)
def recommend_hit():
    print("Other players have higher total")
    print("Recommended to hit")
    messagebox.showinfo("Hit", "Recommended to hit")
 
def recommend_stand():
    print("Recommended to stand")
    messagebox.showinfo("Stand", "Recommended to stand")

def recommend_surrender():
    print("Recommended to surrender")
    messagebox.showinfo("Surrender", "Recommended to surrender")


# Calculate best move based on shoe value
def calculate_best_move(): #custom algorithm
    print("Calculating best move")
    userplayer = players[configuration.playerpos] #get the player that the user is controlling
    print("User player:", userplayer) # debug
    print(cards_in_shoe) 
    calculate_shoe_value() #see calculate_shoe_value
    total_cards = sum(cards_in_shoe.values()) #get the total amount of cards in the shoe
    print("Amount of cards in shoe:", total_cards) #debug
    expected_next_card = shoe_value // total_cards #get the avg expected value of the next card
    print("Expected next card value:", expected_next_card)
    print(holding_ace['dealer']) #test
    if (holding_ace['dealer']) != 0: #if the dealer is holding an ace
        if configuration.surrender_allowed == 'Early' or 'Late': #and if surrender is allowed
            if cards_in_shoe['tvcs'] < 16*configuration.decks:# and if theres at least one TVC on the table
                recommend_surrender() #recommend surrender
                return
            else:
                pass

    
    
    if current_value[userplayer] + expected_next_card > 21: #if the next card will put the user player above 21
        likelybust = True #theyll be likely to bust
        print("Likely bust")
    else:
        likelybust = False #if not, theyre not likely to bust
        print("Not likely to bust")
    if len(players) == 4:
        if userplayer == 'player1':
            workingtotal1 = current_value['player2']
            workingtotal2 = current_value['player3']
        elif userplayer == 'player2':
            workingtotal1 = current_value['player1']
            workingtotal2 = current_value['player3']
        elif userplayer == 'player3':
            workingtotal1 = current_value['player1']
            workingtotal2 = current_value['player2']
        if workingtotal1 or workingtotal2 > current_value[userplayer]:
            recommend_hit() # if the other players have a higher total, recommend hit
    elif len(players) == 3:
        if userplayer == 'player1':
            workingtotal1 = current_value['player2']
        elif userplayer == 'player2':
            workingtotal1 = current_value['player1']
        if workingtotal1 > current_value[userplayer]:
            recommend_hit() # if the other player has a higher total, recommend hit
    elif len(players) == 2 and likelybust == True:
        recommend_stand() # if the user player is likely to bust, and is likely to win even if they dont hit, recommend stand
    else:
        recommend_hit()#else
        





    
    
    

    



    

cbm_button = ctk.CTkButton(master=gameappapp, text="Calculate Best Move", command=calculate_best_move,font=(fontinuse, 12))
cbm_button.pack(side='right', pady=5)


def add_card(player): #custom
    
    def select_card():
        if current_value[player] > 21 and holding_ace[player] == 0:
            print(f"{player} is already bust, cannot select a card")
            playercards[player].config(text="".join("BUST"))
            card_window.destroy()
            return
        elif current_value[player] > 21 and holding_ace[player] > 0:
            current_value[player] -= 10
            holding_ace[player] -= 1
        card = card_combobox.get()
        card_symbol = card_mapping[card]
        
        print(f"{player} selected {card}")
        print(f"Current cards for {player}: {current_cards[player]}")
        if card in ['10', 'Jack', 'Queen', 'King']:
            if cards_in_shoe['tvcs'] == 0:
                print("No more ten valued cards left in shoe")
                return
            else:
                pass
        else:
            if cards_in_shoe[card] == 0:
                print(f"No more {card}s left in shoe")
                return
            else:
                pass
        current_cards[player].append(card_symbol)
        playercards[player].config(text="".join(current_cards[player]))
        if card in ['2', '3', '4', '5', '6', '7', '8', '9']:
            current_value[player] += int(card)
            cards_in_shoe[card] -= 1
            print(cards_in_shoe[card],[card],"cards left in shoe")
        elif card in ['10', 'Jack', 'Queen', 'King']:
            current_value[player] += 10
            cards_in_shoe['tvcs'] -= 1
            print(cards_in_shoe['tvcs'],"TVCs left in shoe")
        elif card == 'Ace':
            current_value[player] += 11
            holding_ace[player] += 1
            cards_in_shoe['Ace'] -= 1
            print(cards_in_shoe['Ace'],"aces left in shoe")
        if current_value[player] > 21 and holding_ace[player] == 0:
            print(f"{player} is already bust, cannot select a card")
            playercards[player].config(text="".join("BUST"))
            card_window.destroy()
            return
        elif current_value[player] > 21 and holding_ace[player] > 0:
            current_value[player] -= 10
            holding_ace[player] -= 1
        card = card_combobox.get()
        card_symbol = card_mapping[card]
        print(f"Current value for {player}: {current_value[player]}","soft" if holding_ace[player] > 0 else "")
        if current_value[player] > 21 and holding_ace[player] >0 :
            current_value[player] -= 10
            holding_ace[player] -= 1 #Accont for the ace being used as 1 or 11
            if current_value[player] > 21:
                return
        elif current_value[player] > 21 and holding_ace[player] == 0:
            print(f"{player} busts")
            playercards[player].config(text="".join("BUST"))
            card_window.destroy()


    card_window = tk.Toplevel(gameappapp)
    card_window.title("Select a card")
    card_window.geometry("200x100")


    card_combobox = ctk.CTkComboBox(master=card_window, values=cardsf, state='readonly', dropdown_font=(fontinuse, 12), width=1)
    card_combobox.pack(pady=10)

    button_frame = tk.Frame(card_window)
    button_frame.pack(pady=5)

    select_button = tk.Button(button_frame, text="Select", command=select_card,font=(fontinuse, 12))
    select_button.pack(side='left', padx=5)

    done_button = tk.Button(button_frame, text="Done", command=card_window.destroy,font=(fontinuse, 12))
    done_button.pack(side='left', padx=5)

    select_button.bind("<Return>", lambda event: select_card(),font=(fontinuse, 12))

def newhand():
    for player in players:
        current_cards[player] = []
        current_value[player] = 0
        holding_ace[player] = False
        playercards[player].config(text="")
        print(f"{player} new hand")
    print("New hand started")
    print(cards_in_shoe)

nh = ctk.CTkButton(master=gameappapp, text="New Hand", command=newhand,font=(fontinuse, 12))
nh.pack(side='left', pady=5)
for player in players:
    user = bool(False)
    if configuration.playerpos == players.index(player):
        user = bool(True)
    print(players.index(player), "- isUser:", user)
    labels[player] = tk.Label(master=gameappapp, text=player, fg='snow', font=(fontinuse, 18),bg='gray20')
    addcard[player] = ctk.CTkButton(master=gameappapp, command=lambda p=player: add_card(p), text="Add Card",font=(fontinuse, 12))
    playercards[player] = tk.Label(master=gameappapp, text="", fg='snow', font=(fontinuse, 72),bg='gray20')
    

youlabel = tk.Label(master=gameappapp, text="You", fg='orange red', font=(fontinuse, 12),bg='gray20')
if configuration.playerpos == 1:
    youlabel.place(anchor='se', relx=0.9, rely=1)
elif configuration.playerpos == 2:
    youlabel.place(anchor='s', relx=0.5, rely=1)
elif configuration.playerpos == 3:
    youlabel.place(anchor='sw', relx=0.1, rely=1)
else:
    print("Invalid player position error")
    gameappapp.destroy()

labels['dealer'].pack(pady=5)


def qu():
    querystring = ("Cards in shoe:\n"
                "Aces: " + str(cards_in_shoe['Ace']) + "\n" +
                   "Twos: " + str(cards_in_shoe['2']) + "\n" +
                   "Threes: " + str(cards_in_shoe['3']) + "\n" +
                   "Fours: " + str(cards_in_shoe['4']) + "\n" +
                   "Fives: " + str(cards_in_shoe['5']) + "\n" +
                   "Sixes: " + str(cards_in_shoe['6']) + "\n" +
                   "Sevens: " + str(cards_in_shoe['7']) + "\n" +
                   "Eights: " + str(cards_in_shoe['8']) + "\n" +
                   "Nines: " + str(cards_in_shoe['9']) + "\n" +
                   "TVCs: " + str(cards_in_shoe['tvcs']))
    messagebox.showinfo("Cards in Shoe", querystring)


query = ctk.CTkButton(master=gameappapp, text="?", command=qu,corner_radius=100,height=2,width=2)
query.place(anchor='ne', relx=0.99, rely=0.01)

# Place player labels at specified locations
labels['player1'].place(anchor='se', relx=0.9, rely=0.967)
if configuration.current_nop >= 2:
    labels['player2'].place(anchor='s', relx=0.5, rely=0.967)
    labels['player2'].configure(fg='orange red')
    addcard['player2'].place(anchor='n', relx=0.5, rely=0.85)
    playercards['player2'].place(anchor='n', relx=0.5, rely=0.62)
    playercards['player2'].configure(fg='orange red')
if configuration.current_nop == 3:
    labels['player3'].place(anchor='sw', relx=0.1, rely=0.967)
    addcard['player3'].place(anchor='n', relx=0.1, rely=0.85)
    playercards['player3'].place(anchor='n', relx=0.175, rely=0.62)


addcard['dealer'].place(anchor='n', relx=0.5, rely=0.054)
addcard['player1'].place(anchor='n', relx=0.9, rely=0.85)
playercards['dealer'].place(anchor='n', relx=0.5, rely=0.1)
playercards['player1'].place(anchor='n', relx=0.825, rely=0.62)

'''def save():
    # dt = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    nameapp = ctk.CTk()
    nameapp.focus_force()
    nameapp.geometry("300x200")
    nameapp.title("Save Game")
    sell = ctk.CTkLabel(master=nameapp, text="Enter a name for the save file", font=(fontinuse, 12))
    sell.pack(pady=5)
    # Create the entry widget for the name
    selectname = ctk.CTkEntry(master=nameapp, corner_radius=100, height=2, width=100,placeholder_text="Enter name")
    selectname.pack(pady=5)

    save_name = ''

    def on_save():
            save_name = ''
            save_name = selectname.get()
            nameapp.destroy()

    # Create the button to save and destroy the nameapp window
    confirm = ctk.CTkButton(
        master=nameapp,
        command=on_save,
        text="Save",
        corner_radius=100,
        height=2,
        width=2
    )
    confirm.pack(pady=5)

    # Start the nameapp event loop
    nameapp.mainloop()

    # Get the entered name after the event loop ends
    print(save_name)

    # Write the configuration to a file with the entered name
    with open(save_name + ".txt", "w") as f:
        f.write(f"Decks: {configuration.decks}\n")

        f.write(f"Decks: {configuration.decks}\n")
        f.write(f"Player Position: {configuration.playerpos}\n")
        f.write(f"Number of Players: {configuration.current_nop}\n")
        f.write("Current Decks:\n")
        for card in cards_in_shoe:
            f.write(f"{card}: {cards_in_shoe[card]}\n")
        f.write(f"Current Player: {players[configuration.playerpos]}\n")
        f.write("Current Cards:\n")
        for player in players:
            f.write(f"{player}: {current_cards[player]}\n")
        f.write("Current Values:\n")
        for player in players:
            f.write(f"{player}: {current_value[player]}\n")
        f.write("Holding Ace:\n")
        for player in players:
            f.write(f"{player}: {holding_ace[player]}\n")
        f.write("Expected Next Card: " + str(expected_next_card))
        f.write("Shoe Value: " + str(shoe_value))
        print("Game saved")
        messagebox.showinfo("Save", "Game saved")
        f.close()'''

def save():
    # Initialize the window
    nameapp = ctk.CTk()
    nameapp.focus_force()
    nameapp.geometry("300x200")
    nameapp.title("Save Game")
    
    # Create the label
    sell = ctk.CTkLabel(master=nameapp, text="Enter a name for the save file", font=(fontinuse, 12))
    sell.pack(pady=5)
    
    # Create the entry widget for the name
    selectname = ctk.CTkEntry(master=nameapp, corner_radius=100, height=2, width=100, placeholder_text="Enter name")
    selectname.pack(pady=5)
    
    # Define the save_name variable in the outer scope
    save_name = None
    

    def saveandexit():
        nameapp.destroy()
        os.exit()
        on_save()

    # Create the button to save and destroy the nameapp window
    def on_save():
        nonlocal save_name
        save_name = selectname.get()
        nameapp.destroy()
        if save_name == '' or save_name == None:
        # Write the configuration to a file with the entered name
            with open(save_name + ".txt", "w") as f:
                f.write(f"{configuration.decks}\n")
                f.write(f"{configuration.playerpos}\n")
                f.write(f"{configuration.current_nop}\n")
                f.write("\n") 
                f.write(str(expected_next_card)+"\n")
                f.write(str(shoe_value)+"\n")
                for card in cards_in_shoe:
                    f.write(f"{cards_in_shoe[card]}\n")
                f.write(f"{players[configuration.playerpos]}\n")
                f.write("\n")
                for player in players:
                    f.write(f"{current_cards[player]}\n")
                    f.write(f"{current_value[player]}\n")
                    f.write(f"{holding_ace[player]}\n")
                print("Game saved")
                messagebox.showinfo("Save", "Game saved")
        else:
            print('You need a name')

    
    confirm = ctk.CTkButton(
        master=nameapp,
        command=on_save,
        text="Save without exiting",
        corner_radius=100,
        height=2,
        width=2
    )
    confirm.pack(pady=5)

    exitsave = ctk.CTkButton(
        master=nameapp,
        command=saveandexit,
        text="Save and exit",
        corner_radius=100,
        height=2,
        width=2
    )
    exitsave.pack(pady=5)

    
    # Start the nameapp event loop
    nameapp.mainloop()



save_button = ctk.CTkButton(master=gameappapp, text="Save Game", command=save,font=(fontinuse, 12))
save_button.place(anchor='nw', relx=0.25, rely=0.95)

exit_button = ctk.CTkButton(master=gameappapp, text= "Exit Game", command=gameappapp.destroy,font=(fontinuse, 12))
exit_button.place(anchor='nw',relx=0.6,rely=0.95)



gameappapp.mainloop()
