import os
from moviepy.editor import *
import tkinter as tk
from tkinter import Tk, filedialog, Button


def file():
    file = filedialog.askopenfilename()
    print(file, type(file))
    convert(file)


def convert(file):
    video = VideoFileClip(os.path.join(file))
    dir1 = os.getcwd()
    video.audio.write_audiofile(os.path.join(dir1, 'output.mp3'))


root = Tk()

btn = Button(text='Convert', command=file, height=5, width=15)

btn.place(x=50, y=50)

filename = 'sweetchildofmeme.mp4'


root.mainloop()
