import os  
from winotify import Notification,audio
from os import getcwd

def alert(Text):
    icon_path = r"C:\Users\ABHISHEK\OneDrive\Desktop\nova\logo.png"

    toast = Notification(
       app_id="N.O.V.A",
       title="⚠️ Alert",
       msg=Text,
       duration="long",
       icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)
    toast.show()


