rom tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

window = Tk()

TopFrame = Frame(window)
BottomFrame = Frame(window)
TopFrame.pack()
BottomFrame.pack()

prompt = ttk.Label(TopFrame,text="Plant Disease Prediction",font=('Times New Roman',16))
prompt.grid(row=0,columnspan = 3,sticky= W)

select_file_prompt = ttk.Label(TopFrame,text="Choose a leaf image to predict it's disease",font=('Times New Roman',15))
select_file_prompt.grid(row=22,sticky=W,padx= 5)

def browsefunc():
    files = [("IMG","*.jpg")]
    browsefunc.filename = filedialog.askopenfilename(filetypes=files,defaultextension = files)
    pathlabel.config(text=browsefunc.filename)

def browsefunc():
    files = [("IMG","*.jpg")]
    browsefunc.filename = filedialog.askopenfilename(filetypes=files,defaultextension = files)
    pathlabel.config(text=browsefunc.filename)

window.title("Plant Disease Prediction")
window.geometry("600x600")

window.mainloop()
