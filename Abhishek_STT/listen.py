# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from deep_translator import GoogleTranslator
# import re
# from os import getcwd, path
# import time

# # Paths
# fake_wav = path.join(getcwd(), "test.wav")
# website = f"{getcwd()}\\index.html"
# rec_file = f"{getcwd()}\\input.txt"

# # Chrome Options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--use-fake-device-for-media-stream")
# chrome_options.add_argument(f"--use-file-for-fake-audio-capture={fake_wav}")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--log-level=3")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# prefs = {
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.notifications": 1,
# }
# chrome_options.add_experimental_option("prefs", prefs)

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install(), log_path="NUL"),
#     options=chrome_options
# )

# website = "https://allorizenproject1.netlify.app/"

# driver.get(website)

# def translate_mixed(text: str) -> str:
#     """Translate Hindi/Hinglish parts into English but keep English as is"""
#     try:
#         # Break sentence into words
#         words = text.split()
#         translated_words = []
#         for w in words:
#             try:
#                 # If word already English (a-z letters), keep it
#                 if re.match("^[a-zA-Z]+$", w):
#                     translated_words.append(w)
#                 else:
#                     # Translate non-English word
#                     trans = GoogleTranslator(source="auto", target="en").translate(w)
#                     translated_words.append(trans)
#             except:
#                 translated_words.append(w)
#         return " ".join(translated_words)
#     except:
#         return text

# def listen():
    
#     try:
#         start_button = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.ID, 'startButton'))
#         )
#         start_button.click()
#         print("Listning...")

#         output_text = ""

#         while True:
#             try:
#                 output_element = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.ID, 'output'))
#                 )
#                 current_text = output_element.text.strip()

#                 if current_text and current_text != output_text:
#                     output_text = current_text

#                     # Translate Hinglish/Hindi → English
#                     english_text = translate_mixed(current_text)

#                     # Save & Print
#                     with open(rec_file, "w", encoding="utf-8") as file:
#                         file.write(english_text.lower())
#                     print("USER :", english_text)

#                     # Stop condition (if 'stop' word appears anywhere)
#                     if english_text.lower().strip() == "stop":
#                         print(" SESSION TERMINATE ")
#                         break

#             except Exception:
#                 pass

#             time.sleep(1)

#     except KeyboardInterrupt:
#         print("\nSESSION TERMINATE")
#     finally:
#         driver.quit()

# listen()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import getcwd
import os
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# Setting up Chrome options with specific arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--headless=new")

# Setting up the Chrome driver with WebDriverManager and options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

 # Creating the URL for the website using the current working directory
website = "https://allorizenproject1.netlify.app/"

 # Opening the website in the Chrome browser
driver.get(website)

Recog_File = f"{getcwd()}\\input.txt"

def listen():
    print("Hello Sir,")
    try:
        start_button = WebDriverWait (driver, 20).until(EC.
        element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait (driver, 10).until(EC.presence_of_element_located((By.ID, 'output'))) 
            current_text = output_element.text.strip()
            time.sleep(0.2)
            if "Start Listening" in start_button.text and is_second_click:
              if output_text:
                  is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
            if current_text != output_text:
               output_text = current_text
               with open (Recog_File, "w") as file:
                 file.write(output_text.lower())
                 print("User: ", output_text)

            if current_text.lower() == "exit":
               print("Session Terminating...")
               driver.quit()
               break
            
    except KeyboardInterrupt:
       pass 
    except Exception as e:
       print("An error occurred:", e)