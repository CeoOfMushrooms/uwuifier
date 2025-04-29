import random
import pyperclip
import os
import platform

LoadedMessage()

def clear_terminal():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    elif system == "Linux" or system == "Darwin":
        os.system('clear')
    else:
        print("Operating system not supported to clear terminal.")

def uwuify(text):
    
    faces = [
        "(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^", "(✿>w<)",
        "(* ^ ω ^)", "(⌒‿⌒)", "(≧◡≦)", "(☆ω☆)", "(⌒ω⌒)", "(✧ω✧)", "(๑>ᴗ<๑)",
        "(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)", "(つ≧▽≦)つ", "(づ｡◕‿‿◕｡)づ", "(≧ω≦)", "(っ◔◡◔)っ",
        "（。＾▽＾）", "owo what's this?", ">//<", "( •̀ ω •́ )✧", "(＾・ω・＾)", "rawr~"
    ]
    
    text = text.replace('r', 'w').replace('l', 'w')
    text = text.replace('R', 'W').replace('L', 'W')
    text = text.replace('no', 'nyo')
    text = text.replace('No', 'Nyo')
    text = text.replace('has', 'haz')
    text = text.replace('have', 'haz')
    text = text.replace('you', 'yuwu')
    text = text.replace('You', 'Yuwu')
    text = text.replace('the', 'da')
    text = text.replace('The', 'Da')
    
    uwu_text = text + "~ " + random.choice(faces)
    return uwu_text
try:

    while True:
        
        user_input = input("Enter text to UwUify (or type 'exit' to quit):\n> ")

        if user_input.lower() == 'exit':
            break
        uwu_text = uwuify(user_input)
        clear_terminal()

        try:
            pyperclip.copy(uwu_text)
            print("Copied to clipboard!")
        except pyperclip.PyperclipException:
            print("Warning: Could not copy to clipboard.")
        
        print("\nUwUified text:\n" + uwu_text)
except KeyboardInterrupt:
    clear_terminal()
    print("\nExited! Bye! (´｡• ᵕ •｡`) ♡")


def LoadedMessage():
    print("Loaded successfully!")