from playsound import playsound
import time
from tkinter import *
from PIL import ImageTk, Image

#----------------Constants-------------------#

char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ",", "?", "'",  "!",  "/",
             "(", ")", ":", ";", "=", "+", "_", '"', "$", "£", "@", " ", "."
             ]

other_list = [" ", "."]

morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
              "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "ñ": "--.--", "o": "---",
              "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
              "x": "-..-", "y": "-.--", "z": "--..", "0": "--..", "1": "--..", "2": "--..", "3": "--..", "4": "--..",
              "5": "--..", "6": "--..", "7": "--..", "8": "--..", "9": "--..", ",": "--..", "?": "--..", "'": "--..",
              "!": "--..", "/": "--..", "(": "--..", ")": "--..", ":": "--..", ";": "-.-.-.", "=": "--..", "+": "--..",
              "-": "--..", '"': "--..", "$": "--..", "£": "--..", "@": "--.."
              }

dot_symbol = {".": ".-.-.-"}

space_symbol = {" ": "▲"}

triangle_symbol = {"▲": "    "}

TEXT = "zas"
NEW_TEXT = "zascazascazasca"
can_translate = True

#----------------Translator mechanism-------------------#

def to_morse():
    tranlation_label.config(text="Translation will come here", bg="white")
    global can_translate, TEXT, NEW_TEXT
    can_translate = True
    untranslatable = []
    TEXT = text_entry.get().lower()
    NEW_TEXT = TEXT.lower()
    for char in NEW_TEXT.lower():
        if char not in char_list:
            untranslatable.append(char)
            can_translate = False

    for key, value in space_symbol.items():
        NEW_TEXT = NEW_TEXT.replace(key, (value))

    for key, value in dot_symbol.items():
        NEW_TEXT = NEW_TEXT.replace(key, (value + " "))

    for key, value in morse_dict.items():
        NEW_TEXT = NEW_TEXT.replace(key, (value + " "))

    for key, value in triangle_symbol.items():
        NEW_TEXT = NEW_TEXT.replace(key, (value))

    if can_translate == False:
        tranlation_label.config(text=f"Please don't use {untranslatable} for this program.", bg="red")
        playsound("23H.mp3")


    else:
        tranlation_label.config(text=NEW_TEXT)


def play():
    for char in NEW_TEXT:
        if char == "-":
            playsound("Fierce Hit.mp3")
        if char == ".":
            playsound("Jab Hit.mp3")
        else:
            playsound("silence.mp3")
    playsound("uggh.mp3")





# -------------User Interface----------------#

window = Tk()
window.title("Morse Translator - Street Fighter Edition")
window.config(padx=20, pady=20, bg="grey12")
window.geometry("1450x250")

logo_frame = Frame(window, width=300, height=50, borderwidth =0)
logo_frame.grid(column=0, row=0, columnspan=2)

img = ImageTk.PhotoImage(Image.open("logo.jpg"))
img_label = Label(logo_frame, image=img, borderwidth =0)
img_label.pack()

text_entry = Entry(window, width=80, font=("Arial", 18))
text_entry.focus()
text_entry.grid(column=1, row=1, padx=10, pady=10)

translate_button = Button(text="Translate", highlightthickness=0, width=10, height=1, font=("Arial", 14), command=to_morse)
window.bind("<Return>", lambda event:to_morse())
translate_button.grid(column=0, row=1, padx=10, pady=10)

play_button = Button(text="Play", highlightthickness=0, width=10, height=1, font=("Arial", 14), command=play)
window.bind("<Shift_L>", lambda event:play())
play_button.grid(column=0, row=2, padx=10, pady=10)

tranlation_label = Label(window, text="Translation will come here", width=105, height=1, font=("Lucida Console", 14, "bold"))
tranlation_label.grid(column=1, row=2, padx=10, pady=10)

window.mainloop()
