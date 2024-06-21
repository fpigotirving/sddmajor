import tkinter as tk
import customtkinter as ctk
'''import os'''
import configuration
'''import subprocess
from subprocess import call
import sys
import time'''



setapp = ctk.CTk()
setapp.focus_force()
setapp.geometry("300x400+200+200")
setapp.title("")
def test_button():
        print("function called")
title = ctk.CTkLabel(master=setapp, text="Options", font=("Menlo", 18))
title.pack(anchor=ctk.N,pady=15)



'''insurancelabel = ctk.CTkLabel(master=setapp, text="Insurance Pays")
insurancelabel.pack(anchor=ctk.N,pady=5)
inspay = ctk.CTkComboBox(master=setapp, values=configuration.insurance_pays,state='readonly')
inspay.pack(anchor=ctk.N,pady=5)
inspay.set(configuration.selinspay)
configuration.selinspay = selection = inspay.get()'''

ds17label = ctk.CTkLabel(master=setapp, text="Soft 17 Dealer Behaviour")
ds17label.pack(anchor=ctk.N,pady=5)
ds17 = ctk.CTkComboBox(master=setapp, values=configuration.soft17_dealer_behaviour,state='readonly')
ds17.pack(anchor=ctk.N,pady=5)
ds17.set(configuration.selsoft17dealerbehaviour)
configuration.selsoft17dealerbehaviour = selection = ds17.get()
surrl = ctk.CTkLabel(master=setapp, text="Surrender Allowed")
surrl.pack(anchor=ctk.N,pady=5)
surr = ctk.CTkComboBox(master=setapp, values=configuration.surrender_allowed,state='readonly')
surr.pack(anchor=ctk.N,pady=5)
surr.set(configuration.selsurrenderallowed)
configuration.selsurrenderallowed = selection = surr.get()

dysfontlabel = ctk.CTkLabel(master=setapp, text="Font")
dysfontlabel.pack(anchor=ctk.N,pady=5)
dysfont = ctk.CTkComboBox(master=setapp, values=configuration.fonts,state='readonly')
dysfont.pack(anchor=ctk.N,pady=5)
dysfont.set(configuration.fonts[0])



'''def s():
    configuration.selinspay = selection = inspay.get()
    print(configuration.selinspay)
printcurrentinsurancepaystatus = ctk.CTkButton(master=setapp, command=s, text="Print Current Insurance Pay Status")
printcurrentinsurancepaystatus.pack(anchor=ctk.N,pady=10)'''
def kill():
    configuration.selsoft17dealerbehaviour = selection = ds17.get()
    configuration.selsurrenderallowed = selection = surr.get()
    configuration.selected_font = selection = dysfont.get()
    setapp.destroy()

end = ctk.CTkButton(master=setapp, command=kill, text="Done")
end.pack(anchor=ctk.S,pady=10)
'''button = ctk.CTkButton(master=setapp, command=test_button, text="Click Me")
button.pack(anchor=ctk.N)'''

setapp.mainloop()