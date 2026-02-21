import threading
from internet_check import is_Online
from Alert import alert
from data.DLG_Data import online_dlg,offline_dlg
import random
from co_joanna import Nova
from TextToSpeech.ttsB import speak
from Automation.battery import check_plug
from Time_Operations.brain import input_manage
from Time_Operations.throw_alert import check_schedule,check_Alarm
import time

Alarm_path = r"C:\Users\ABHISHEK\OneDrive\Desktop\nova\Alarm_data.txt"
file_path = r'C:\Users\ABHISHEK\OneDrive\Desktop\nova\schedule.txt'

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)
       
# def main():
#      if is_Online():
#         t1 = threading.Thread(target=speak,args=(ran_online_dlg,))
#         t2 = threading.Thread(target=alert,args=(ran_online_dlg,))
#         t3 = threading.Thread(target=check_plug)
#         t4 = threading.Thread(target=check_schedule,args=(file_path,))
#         t5 = threading.Thread(target=Nova)
#         t6 = threading.Thread(target=check_Alarm,args=(Alarm_path,))
#         t1.start()
#         t2.start()
#         t1.join()
#         t2.join()
#         t3.start()
#         t4.start()
#         t5.start()
#         t6.start()
#         t3.join()
#         t4.join()
#         t5.join()
#         t6.join()
        
#         time.sleep(0.3)
        
#      else:
#        alert(ran_offline_dlg)
      
def main():
    if is_Online():
        threading.Thread(target=speak, args=(ran_online_dlg,), daemon=True).start()
        threading.Thread(target=alert, args=(ran_online_dlg,), daemon=True).start()

        threading.Thread(target=check_plug, daemon=True).start()
        threading.Thread(target=check_schedule, args=(file_path,), daemon=True).start()
        threading.Thread(target=check_Alarm, args=(Alarm_path,), daemon=True).start()
        threading.Thread(target=Nova, daemon=True).start()

        while True:
            time.sleep(1)
    else:
        alert(ran_offline_dlg)

main()