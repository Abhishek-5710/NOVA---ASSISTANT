# import requests
# import pygame
# import os
# from urllib.parse import quote
# import uuid
# import time

# # --- Config ---
# VOICE = "Joanna"   # female voice, try "Amy" or "Joanna"
# OUT_DIR = r"C:\Users\ABHISHEK\OneDrive\Desktop\nova\TextToSpeech"
# os.makedirs(OUT_DIR, exist_ok=True)

# def generate_audio(message: str, voice: str = VOICE):
#     text = quote(message)
#     url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={text}"
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     r = requests.get(url, headers=headers, timeout=15)
#     return r

# def speak(message: str, voice: str = VOICE, out_dir: str = OUT_DIR):
#     r = generate_audio(message, voice)
    
#     # check response
#     if r.status_code != 200:
#         try:
#             print("Error response:", r.json())
#         except Exception:
#             print("Error body (first 500 chars):", r.text[:500])
#         return

#     ctype = r.headers.get("Content-Type", "")
#     if not ctype.startswith("audio"):
#         print("Response is not audio. Content-Type:", ctype)
#         print("Body (first 500):", r.text[:500])
#         return

#     # unique filename to avoid MCI / path issues
#     unique_name = f"{voice}_{uuid.uuid4().hex}.mp3"
#     file_path = os.path.join(out_dir, unique_name)

#     # save file
#     with open(file_path, "wb") as f:
#         f.write(r.content)
#         f.flush()
#         os.fsync(f.fileno())
#     time.sleep(0.05)  # small delay for filesystem

#     try:
#         # play using pygame
#         pygame.mixer.init()
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#           pygame.time.Clock().tick(30)
#     except Exception as e:
#         print("Playback error:", e)
#     finally:
#         # remove file safely
#         for _ in range(6):
#             try:
#                 os.remove(file_path)
#                 break
#             except PermissionError:
#                 time.sleep(0.1)
#         try:
#             pygame.mixer.quit()
#         except:
#             pass

import pyttsx3
import threading

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # female
engine.setProperty("rate", 175)

_tts_lock = threading.Lock()

def speak(text):
    with _tts_lock:
        engine.say(text)
        engine.runAndWait()
