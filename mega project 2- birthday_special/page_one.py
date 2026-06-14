import customtkinter as ctk
from PIL import Image, ImageTk
import pygame
import tkinter as tk
import random
import time
import os
import streamlit as st

#window
app = ctk.CTk()
app.title("birthday gift!!")
app.geometry("800x600")
app.state("zoomed")
#password
correct_password = "2007"

#functions
def check_password():
    if password_entry.get()== correct_password:
         show_birthday_page()

    else:
        result_label.configure(text="❌ Wrong Password!")

def show_suprise():
     surprise_label= ctk.CTkLabel(
          app,
          text="You are one of the most important people in my life ❤️",
          font=("Arial",24,"bold"
                )
     )
     surprise_label.pack(pady=20)
def show_birthday_page( ):
       
    # Remove everything from page 1 
       for widget in app.winfo_children():
            widget.destroy()
       
     #Birthday title
       birthday_title = ctk.CTkLabel( 
          app,
          text="""🎉 HAPPY BIRTHDAY Dear! 🎉

Thank you for always being such an amazing friend.
May this year bring you happiness,
success, and lots of cake. 🎂""",
          font = ("Arial",40,"bold")
                    )  
       birthday_title.pack(pady=40)
            
            # cake
       cake=ctk.CTkLabel(
                    app,
                    text="🎂",
                    font=("Arial",90)
)       
       cake.pack(pady=20 )       
       message = ctk.CTkLabel(
          app,
         text="""Dear Friend,

Wishing you a very Happy Birthday! 🎉

May your day be filled with happiness,
laughter, success, and lots of cake. 🎂

Thank you for being such an amazing friend.

Enjoy your special day! ❤️
""",
            font=("Arial", 20)
)

       message.pack(pady=20)
#title
title= ctk.CTkLabel(
    app,
    text= "🎁 SECRET BIRTHDAY GIFT 🎁",
     font =("Arial",30,"bold")
     )

title.pack(pady=30)

# instruction
instruction= ctk.CTkLabel(
    app,
    text= "Enter the secret password"
)                 
instruction.pack(pady=30)
#password box
password_entry= ctk.CTkEntry(
    app,
    show="*",
    width=250
)
password_entry.pack(pady=10)

#button
button=ctk.CTkButton(
    app,
    text="💌 Open Letter",
    command=check_password
)
button.pack(pady=20)
# Result
result_label= ctk.CTkLabel(
    app,
    text=""
)
result_label.pack(pady=10)

#run
app.mainloop()





















































