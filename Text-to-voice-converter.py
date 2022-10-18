import time
from gtts import gTTS
import os
from tkinter import *
import sv_ttk

def text_to_voice():
    file_name = file_name_entry.get()
    text_to_convert = choose_entry.get()
    time.sleep(1)
    language = "en"
    voice_object = gTTS(text=text_to_convert, lang=language, slow=True)
    voice_object.save(f"new_sound_{file_name}.mp3")
    finished_label.config(text="success! the audio file is waiting for you")



window = Tk()
sv_ttk.set_theme("light")
window.title("Text to Voice Software")
window.config(padx=100, pady=50)

canvas = Canvas(width=500, height=400, highlightthickness=0)
mic_image = PhotoImage(file="mic.png")
lets_go_button = PhotoImage(file="letts go.png")
canvas_image = canvas.create_image(350, 250, image=mic_image)
canvas.grid(column=0, row=4)

welcome_label = Label(text="Hello, and welcome to the Text-to-Voice software", font=("david", 40))
welcome_label.grid(column=0, row=0, columnspan=2, sticky="e")

space_label = Label(text="")
space_label.grid(column=0, row=1)

choose_label = Label(text="enter your text:", font=("david", 20))
choose_label.grid(column=0, row=2, columnspan=1)

choose_entry = Entry(width=90)
choose_entry.insert(END, string="")
choose_entry.grid(column=1, row=2, columnspan=1)

file_name_label = Label(text="file name:", font=("david", 20))
file_name_label.grid(column=0, row=3, columnspan=1)

file_name_entry = Entry(width=90)
file_name_entry.insert(END, string="")
file_name_entry.grid(column=1, row=3, columnspan=1)

choose_text_button = Button(image=lets_go_button, bd=0, command=text_to_voice)
choose_text_button.grid(column=1, row=4)

finished_label = Label(text="", font=("david", 16), padx=20, pady=20)
finished_label.grid(column=0, row=5, columnspan=2)

window.mainloop()
