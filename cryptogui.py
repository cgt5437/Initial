import re
from tkinter import *

def initialize(master, ct):
    global ciphertext, guessDict, text, ptext, ctext

    ciphertext = ct
    guessDict = {}

    frame = Frame(master)
    frame.pack(fill=x)

    text = Text(frame,height=2)
    text.pack(side=TOP,fill=BOTH)
    showtext()

    frame2 = Frame(frame)
    frame2.pack(side=BOTTOM,fill=x)

    label = Label (frame2, text="Ciphertext" )
    label.pack(side=LEFT)

    ptext = Entry(frame2, width=1)
    ptext.pack(side=left)

    label = Label ( frame2, text="Plaintext")
    label.pack(side=LEFT)

    ctext = Entry (frame2, width=1)
    ctext.pack( side=LEFT)

    pad = Label (frame2, text=" ")
    pad.pack ( side=LEFT)

    button = Button( frame2, text="Guess", command=guess )
    button.pack ( side=LEFT)

    quit = Button( frame2, text="Quit", fg="red", command=frame.quit )
    quit.pack(side=RIGHT)

    ptext.focus_set()

def showtext():
    plaintext = translate()

    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(END, plaintext)
    text.insert(END,ciphertext )
    text.config(state=DISABLED)


def translate():
    retval = ''
    for ch in ciphertext:
        if not re.match('[a-z]$', ch):
            retval = retval + ch
        else:
            retval = retval +guessDict.get (ch, '-')

    return retval

def guess():
    global guessDict, ptext, ctext

    pletter = ptext.get()
    cletter = ctext.get()

    if len(pletter)== and len(cletter)==1:
        guessDict[pletter] = cletter

    if len(pletter)==1 and len (cletter)==0:
        if pletter in guessDict:
            delguessDict[pletter]
    showtext()

root = Tk()

initialize( root, ' bq hjtkbrw, b xdbql fdbtenjq zdp jynq wjnbx hyekja ynj lqpzq ya hnraajta afprxa.\n' )

root.mainloop()
