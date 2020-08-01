import os
from moviepy.editor import *
import tkinter as tk
from tkinter import Tk, filedialog, Button, Entry, StringVar


def file():
    file = filedialog.askopenfilename()
    print(file, type(file))
    convert(file)


def convert(file):
    nameOut = nameVar.get()

    video = VideoFileClip(os.path.join(file))
    dir1 = os.getcwd()
    video.audio.write_audiofile(os.path.join(dir1 + '/' + nameOut + '.mp3'))


root = Tk()

nameVar = StringVar(root)

btn = Button(text='Convert', command=file, height=5, width=15)
name = Entry(width=15, textvariable=nameVar)

btn.place(x=50, y=50)
name.place(x=60, y=20, height=25)


root.mainloop()
