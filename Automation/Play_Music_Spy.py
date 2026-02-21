import subprocess
# import webbrowser
import pyautogui as gui
import time

def open_App(app_name):
    try:
      subprocess.run(app_name)
    except Exception as e:
       gui.press("win")
       time.sleep(0.2)
       gui.write(app_name)
       time.sleep(0.2)
       gui.press("enter")


def play_music_on_spotify(song_name):
    open_App("Spotify")
    time.sleep(7)
    gui.hotkey("ctrl","k")
    time.sleep(0.2)
    gui.write(song_name)
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(1.5)           # wait results
    gui.press("tab")          # jump to results
    time.sleep(0.2)
    gui.press("enter") 
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(0.8)
    gui.press("enter")

# open_App("Spotify")
# play_music_on_spotify("Jonny Jonny")