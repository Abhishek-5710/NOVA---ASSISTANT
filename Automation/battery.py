import psutil
import time
import time
from TextToSpeech.ttsB import speak
from Alert import alert
import threading 


battery = psutil.sensors_battery()

def battery_Alert():
    while True:
        percentage = int(battery.percent)
        if percentage == 100:
            t1 = threading.Thread(target=alert,args=("100%charge",))
            t2 = threading.Thread(target=speak,args=("100%charge. please unplug it.",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 20:
            t1 = threading.Thread(target=alert,args=("Low Battery⚠️",))
            t2 = threading.Thread(target=speak,args=("Sorry for disturbing Sir but you Power is low!",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 10:
            t1 = threading.Thread(target=alert,args=("Last Alert sir!",))
            t2 = threading.Thread(target=speak,args=("This is 'FINAL CALL' sir Your battery is too low!",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        time.sleep(10)
     


def check_plug():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged
    while True:
       battery = psutil.sensors_battery()
       if battery.power_plugged != previous_state:
           if battery.power_plugged:
               t1 = threading.Thread(target=alert,args=("PLUGGED IN⚠️",))
               t2 = threading.Thread(target=speak,args=("Charging Started",))
               t1.start()
               t2.start()
               t1.join()
               t2.join()
           else:
                t1 = threading.Thread(target=alert,args=("PLUGGED OUT⚠️",))
                t2 = threading.Thread(target=speak,args=("Charging Stopped",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()

           previous_state = battery.power_plugged

def check_percentage():
     battery = psutil.sensors_battery()
