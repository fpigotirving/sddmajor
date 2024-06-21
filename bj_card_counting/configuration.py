import tkinter as Tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.font as font
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
decks = int()
playerpos = int()
current_nop = int()
current_decks = {} #dictionary to store the number of each card in the deck

loadeddealercards = []
loadedplayer1cards = []
loadedplayer2cards = []
loadedplayer3cards = []
loadeddealerhandvalue = int()
loadeddealeraces = int()
loadedplayer1handvalue = int()
loadedplayer1aces = int()
loadedplayer2handvalue = int()
loadedplayer2aces = int()
loadedplayer3handvalue = int()
loadedplayer3aces = int()

game_source = "New"

insurance_pays = ['2 to 1','3 to 2']   #etc
selinspay = insurance_pays[0]
soft17_dealer_behaviour = ['hits','stands']
selsoft17dealerbehaviour = soft17_dealer_behaviour[0]
surrender_allowed = ['Off', 'Late', 'Early',]
selsurrenderallowed = surrender_allowed[1]
fonts = ['Menlo','Helvetica','Arial','Times New Roman','Courier New','Comic Sans MS']
selected_font = ''

selplayers = int()

initial_counts = {}
cards = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes', 'sevens', 'eights', 'nines','tvcs']

for card in cards:
    initial_counts[card] = 0

