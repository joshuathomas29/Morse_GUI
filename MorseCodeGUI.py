from tkinter import *
from gpiozero import LED
from time import sleep

# Define LED
led = LED(23)

# Define morse code dictionary - taken from https://www.geeksforgeeks.org/morse-code-translator-python/
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

# Create GUI
master = Tk()
master.title("Morse Code")
master.geometry("300x60")

# define dot and dash LED blinks
def morseDot():
    led.on()
    sleep(0.25)
    led.off()
    sleep(0.25)
    
def morseDash():
    led.on()
    sleep(0.75)
    led.off()
    sleep(0.25)

# encryption based off https://www.geeksforgeeks.org/morse-code-translator-python/
def encrypt(message):
    cipher = ''
    for letter in message:
        cipher += MORSE_CODE_DICT[letter] + ' '
    return cipher

# limit entry box character limit - answer from DorinPopescu
# (https://stackoverflow.com/questions/33518978/python-how-to-limit-an-entry-box-to-2-characters-max)
# also limit to no spaces
def limitCharLength(*args):
    entry_text.set(entry_text.get().replace(" ",""))
    value = entry_text.get()
    if len(value) > 12: entry_text.set(value[:12])

entry_text = StringVar()
entry_text.trace('w', limitCharLength)
e = Entry(master, textvariable=entry_text)

e.pack()

# sets entry text to focus when GUI is main focus
e.focus_set()

def callback():
    print("Message: " + e.get())
    message = encrypt(e.get().upper())
    # show morse in terminal
    print("Blinking: " + message)
    for letter in message:
        #if dot call morseDot, if dash call morseDash, else sleep for character separation time
        if letter == ".":
            morseDot()
        elif letter == "-":
            morseDash()
        else:
            sleep(0.75)

b = Button(master, text="Blink Morse LED", width=15, command=callback)
b.pack()

def close():
    led.close()
    window.destroy()
        
master.protocol("WM_DELETE_PROTOCOL", close)
master.mainloop()
