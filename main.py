from sys import path
from tkinter import *
from tkinter.messagebox import *
import tkinter.font as font
import os
import random

# set window title
gui = Tk(className='Random Pokemon Idea')
# set window size
gui.geometry("1280x720")

#Font 
txtfont = font.Font(family='Helvitica', size=20)
btnfont = font.Font(family='Helvitica', size=15)

#Text display
Type1 = Label(gui, text="Type 1", font=txtfont)
Type1.pack()
Type2 = Label(gui, text="Type 2", font=txtfont)
Type2.pack()
creatures = Label(gui, text="Creature", font=txtfont)
creatures.pack()

#Randome selector & label editor
def randtype():
    words = ['Normal', 'Fire', 'Water', 'Grass', 'Flying', 'Fighting', 'Poison', 'Electric',
             'Ground', 'Rock', 'Psychic', 'Ice', 'Bug', 'Ghost', 'Steel', 'Dragon', 'Dark', 'Fairy']
    
    word1 = random.choice(words)
    Type1.config(text=word1)
    print(word1)

    r1 = random.randint(1, 10)
    if (r1 > 8):
        word2 = random.choice(words)
        Type2.config(text=word2)
        print(word2)
    else:
        Type2.config(text=' ')
        print('none')
    
    cryptids = ['Typhons', 'Harpies', 'Gorgones', 'Érinye', 'Scylla', 'Chimères', 
            'Centaures', 'Wendigos', 'Guivres','Goules','Béhémot','Banshee','Rokh','Jiangshi',
            'Leprechaun', 'Kraken', 'Wyvernes', 'Mandragore','Cocatrix', 'Phénix','Mimic',
            'Slimes','Liches', 'Licorne', 'Sphinx', 'Golem', 'Manticore', 'Nagas', 'Inugami']
    cryptid = random.choice(cryptids)
    creatures.config(text=cryptid)
    print(cryptid)

    print('===========================')

#Button
randtypebtn = Button(
    gui, text='Randome Pokemon Type', command=randtype, 
    bg='#f44336', fg='#ffffff', bd=0, font=btnfont
    )

randtypebtn.pack(ipadx=5, ipady=5, expand=True)

# Creat window
gui.mainloop()
