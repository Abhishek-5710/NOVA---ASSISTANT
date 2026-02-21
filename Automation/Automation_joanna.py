from Automation.open_App import open_App
from Automation.web_Open import openweb
import pyautogui as gui 
from Automation.Play_Music_YT import play_music_on_youtube
from TextToSpeech import ttsB
from Automation.Play_Music_Spy import open_App,play_music_on_spotify
from os import getcwd
import time
from Automation.tab_automation import perform_action
from Automation.youtube_playback import perform_media_action
import pywhatkit

def play():
   gui.press("space")

def search_google(text):
    pywhatkit.search(text)

def close():
    gui.hotkey('alt', 'f4')

def search(text):
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)

def Open_Joanna(text):
    if "website" in text or "open website named" in text:
        text = text.replace("open","").strip()
        text = text.replace("open website named","").strip()
        openweb(text)
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        open_App(text)
         
# while True:
#     x = input("Hukum mere aaka : ")
#     Open_Joanna(x)

def clear_file():
     with open(f"{getcwd()}\\input.txt", "w") as file:
        file.truncate(0)

def Auto_main_Jaonna(text):
  try:
    
    text = text.lower().strip()

    if text.startswith("open"):
        Open_Joanna(text)
    elif "close" in text:
        close()
    elif "play on youtube " in text or "play music on youtube" in text:
        ttsB.speak("which song do you want to play sir")
        clear_file()
        if "i don't want" in text:
            pass 
        else:
         clear_file()
         output_text = ""
         while True:
            with open(f"{getcwd()}\\input.txt","r") as file:
               input_text = file.read().lower().strip()
            if input_text != output_text:
               output_text = input_text
               if output_text:
                  play_music_on_youtube(output_text)
                  break
         else:
            pass 

    elif "spotify" in text and ("play" in text or "music" in text):
        ttsB.speak("which song do you want to play sir")
        clear_file()
        output_text = ""
        while True:
            with open(f"{getcwd()}\\input.txt","r") as file:
               input_text = file.read().lower().strip()
            if input_text != output_text:
               output_text = input_text
               if output_text:
                  play_music_on_spotify(output_text)
                  break
        
    elif text.startswith("search"):
        text = text.replace("search","")
        text = text.strip()
        search(text)
        time.sleep(0.5)
        gui.press("enter")
    elif "search in google" in text:
       text = text.replace("search in google", "")
       search_google(text)
    elif "play" in text or "stop" in text or "pause" in text:
       play()

    else:
        perform_action(text)
        perform_media_action(text)

  except Exception as e:
      print("error : " + e)