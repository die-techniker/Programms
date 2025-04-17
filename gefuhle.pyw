#!/usr/bin/python3

import random
from tkinter import *
from tkinter import messagebox
import sys, time
# Event-Funktionen
def button1Click() :
	print("Button „Gut“:\nDas freut mich!")
	Button4.pack()
	Button5.pack()
def button2Click() :
	print("Button „Schlecht“:\n Das tut mir leid!")
	Button4.pack()
	Button5.pack()
def button3Click() :
	print("Button „Mittel“:\nOK!")
	Button4.pack()
	Button5.pack()
def button4Click() :
	print("Button „OK“:\nexit")
	sys.exit()
def button5Click() :
	GEFÜHL = random.choice(["Mir geht es schlecht. \nIch muss auf allen Computern arbeiten und das ist schwer.","Mir geht es gut. \nIch kann gerade ausruhen, weil ich zurzeit wenig zu tun habe.","Mir geht es Mittel.\nIch habe gerade keine schwere Leistung."])
	print("Button „Und wie geht es dir?”\n",GEFÜHL)
# Hauptprogramm
Fenster = Tk()
Anzeige = Label(Fenster, text="Hallo, wie geht es?")
Anzeige.pack()
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button3 = Button(Fenster, text="Mittel", command=button3Click)
Button4 = Button(Fenster, text="OK", command=button4Click)
Button5 = Button(Fenster, text="Und wie geht es dir?", command=button5Click)
Button1.pack()
Button3.pack()
Button2.pack()
Fenster.mainloop()