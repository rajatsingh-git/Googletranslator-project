#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install googletrans==4.0.0-rc1')
get_ipython().system('pip install pillow')


# In[2]:


from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Google Translator")
root.geometry("1080x500")
root.resizable(False, False)
root.configure(background="white")

def label_change():
    lang1 = cg1.get()
    lang2 = cg2.get()
    label1.configure(text=lang1)
    label2.configure(text=lang2)
    root.after(500, label_change)

def translate():
    text_ = text1.get(1.0, END)
    t = Translator()
    trans_text = t.translate(text_, src=cg1.get(), dest=cg2.get())
    trans_text = trans_text.text
    
    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# GUI components
image_path = r"C:\Users\9896j\Downloads\hello.png"
try:
    image = Image.open(image_path)
    arrow_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=arrow_image)
    image_label.place(x=300, y=100)
except Exception as e:
    print(f"Error loading image: {e}")
    arrow_image = None

languageV = list(LANGUAGES.values())

# First language selection
cg1 = ttk.Combobox(root, values=languageV, font="arial")
cg1.place(x=110, y=20)
cg1.set("en")  # Using language code instead of full name

label1 = Label(root, text="ENGLISH", font="arial 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Second language selection
cg2 = ttk.Combobox(root, values=languageV, font="arial")
cg2.place(x=730, y=20)
cg2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="arial 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=630, y=50)

# First text box
frame1 = Frame(root, bg="black", bd=5)
frame1.place(x=10, y=119, width=436, height=200)

text1 = Text(frame1, font="arial", bg='white', relief=GROOVE, wrap=WORD)
text1.pack(expand=True, fill=BOTH)

scroll1 = Scrollbar(frame1, command=text1.yview)
scroll1.pack(side=RIGHT, fill=Y)
text1.config(yscrollcommand=scroll1.set)

# Second text box
frame2 = Frame(root, bg="black", bd=5)
frame2.place(x=630, y=119, width=436, height=200)

text2 = Text(frame2, font="arial", bg='white', relief=GROOVE, wrap=WORD)
text2.pack(expand=True, fill=BOTH)

scroll2 = Scrollbar(frame2, command=text2.yview)
scroll2.pack(side=RIGHT, fill=Y)
text2.config(yscrollcommand=scroll2.set)

# Translate button
translate_button = Button(root, text="Translate", font="arial", activebackground="white", cursor="hand2",
                          bd=2, width=12, height=2, bg='blue', fg='white', command=translate)
translate_button.place(x=470, y=250)

# Start label update function
label_change()

root.mainloop()


# In[ ]:




