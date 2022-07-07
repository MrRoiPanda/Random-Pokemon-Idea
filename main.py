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

#print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))
#gui.iconbitmap(os.path.dirname(os.path.abspath(__file__)) + "/favicon/favicon.ico")

#Top menu
#menubar = Menu(gui)
#
#menuFile = Menu(menubar, tearoff=0)
#menuFile.add_command(label="Creat")
#menuFile.add_command(label="Edit")
#menuFile.add_separator()
#menuFile.add_command(label="Quit", command=gui.quit)
#menubar.add_cascade(label="File", menu=menuFile)
#
#menuTest = Menu(menubar, tearoff=0)
#menuTest.add_command(label="Pré-test")
#menuTest.add_command(label="Test Annuel")
#menuTest.add_separator()
#menuTest.add_command(label="Nouveau Test")
#menuTest.add_command(label="Test Actuel")
#menubar.add_cascade(label="Test", menu=menuTest)
#
#menuHelp = Menu(menubar, tearoff=0)
#menuHelp.add_command(label="Utilisation")
#menuHelp.add_separator()
#menuHelp.add_command(label="About")
#menubar.add_cascade(label="Help", menu=menuHelp)
#
#gui.config(menu=menubar)

Type1 = Label(gui, text="Type 1", font=txtfont)
Type1.pack()
Type2 = Label(gui, text="Type 2", font=txtfont)
Type2.pack()
creatures = Label(gui, text="Creature", font=txtfont)
creatures.pack()

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


randtypebtn = Button(
    gui, text='Randome Pokemon Type', command=randtype, 
    bg='#f44336', fg='#ffffff', bd=0, font=btnfont
    )

randtypebtn.pack(ipadx=5, ipady=5, expand=True)

# Creat window
gui.mainloop()
