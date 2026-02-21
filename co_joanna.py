from Automation.Automation_joanna import Auto_main_Jaonna,clear_file
from Abhishek_STT.listen import listen
from TextToSpeech.ttsB import speak
import threading
import os
from internet_check import is_Online
from Alert import alert
from data.DLG_Data import online_dlg,offline_dlg
import random
from Automation.battery import battery_Alert
from Time_Operations.brain import input_manage,input_manage_Alarm

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

numbers = ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:"]
spl_numbers = ["11:", "12:"]
ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)


def check_inputs():
     output_text = ""
     while True:
          with open("input.txt","r") as file:
               input_text = file.read().lower()
          if input_text != output_text:
               output_text = input_text
          if output_text.startswith("tell me"):
                    output_text = output_text.replace(" p.m.", "PM")
                    output_text = output_text.replace(" a.m.", "AM")
                    if "11:" in output_text or "12:" in output_text:
                         input_manage(output_text)  
                         clear_file() 
                    else: 
                      for number in numbers:
                        if number in output_text:
                           output_text = output_text.replace(number,f"0{number}")
                           input_manage(output_text)  
                           clear_file()   
          elif output_text.startswith("set alarm"):
                    output_text = output_text.replace(" p.m.", "PM")
                    output_text = output_text.replace(" a.m.", "AM")
                    if "11:" in output_text or "12:" in output_text:
                         input_manage_Alarm(output_text)  
                         clear_file() 
                    else: 
                      for number in numbers:
                        if number in output_text:
                           output_text = output_text.replace(number,f"0{number}")
                           input_manage_Alarm(output_text)  
                           clear_file()    
          else:
              Auto_main_Jaonna(output_text)

def Nova():
     clear_file()
     t1 = threading.Thread(target=listen)
     t2 = threading.Thread(target=check_inputs)
     t1.start()
     t2.start()
     t1.join()
     t2.join()

