# import os
# import time
# import threading
# from Alert import alert
# from TextToSpeech.ttsB import speak
# import threading
# from Time_Operations.brain import input_manage
# from os import getcwd

# def load_schedule(file_path):
#     schedule = {}
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 if '=' in line:
#                     line_time, activity = line.strip().split(' = ')
#                     schedule[line_time.strip()] = activity.strip()
#     except Exception as e:
#         print(f"Error loading schedule: {e}")
#     return schedule

# def check_schedule(file_path):
#     last_modified = 0
#     while True:
#         current_time = time.strftime("%I:%M%p")
#         try:
#             # Check file modification time
#             modified = os.path.getmtime(file_path)
#             if modified != last_modified:
#                 last_modified = modified
#                 schedule = load_schedule(file_path)
            
#             if current_time in schedule:
#                 text = schedule[current_time]
#                 t1 = threading.Thread(target=alert, args=(text,))
#                 t2 = threading.Thread(target=speak, args=(text,))
#                 t1.start()
#                 t2.start()
#                 t1.join()
#                 t2.join()
        
#         except Exception as e:
#             print(f"Error: {e}")
        
#         time.sleep(10)


# def load_Alarm_time(file_path):
#     schedule = {}
#     try:
#         with open(file_path, 'r') as file:
#             schedule = file.read()
#             # for line in file:
#             #     if '=' in line:
#             #         t, msg = line.strip().split(' = ')
#             #         schedule[t.replace(" ", "")] = msg
#     except Exception as e:
#         print(f"Error loading alarm: {e}")
#     return schedule


# Alarm_path = r"C:\Users\ABHISHEK\OneDrive\Desktop\nova\Alarm_data.txt"

# # def check_Alarm(Alarm_path):
# #     last_triggered = None
# #     while True:
# #         current_time = time.strftime("%I:%M%p")
# #         # try:
# #         #     # Check file modification time
# #         #     modified = os.path.getmtime(Alarm_path)
# #         #     if modified != last_modified:
# #         #         last_modified = modified
# #         schedule = load_Alarm_time(Alarm_path)
            
# #         if current_time in schedule and current_time != last_triggered:
# #                 text = "This is Alarm"
# #                 text = schedule[current_time]
# #                 t1 = threading.Thread(target=alert, args=(text,))
# #                 t2 = threading.Thread(target=speak, args=(text,))
# #                 t1.start()
# #                 t2.start()
# #                 t1.join()
# #                 t2.join()
# #                 last_triggered = current_time
# #         time.sleep(10)
# # #         # except Exception as e:
# # #         #     print(f"Error: {e}")
        

import time
import threading
from Alert import alert
from TextToSpeech.ttsB import speak

def load_schedule(file_path):
    schedule = {}
    with open(file_path, "r") as f:
        for line in f:
            if "=" in line:
                t, msg = line.strip().split("=", 1)
                schedule[t.replace(" ", "")] = msg.strip()
    return schedule


def check_schedule(file_path):
    triggered = set()

    while True:
        current_time = time.strftime("%I:%M%p")

        schedule = load_schedule(file_path)

        if current_time in schedule and current_time not in triggered:
            text = schedule[current_time]

            threading.Thread(target=alert, args=(text,), daemon=True).start()
            threading.Thread(target=speak, args=(text,), daemon=True).start()

            triggered.add(current_time)

        time.sleep(10)  # 🔥 second-level precision


def check_Alarm(file_path):
    triggered = set()

    while True:
        current_time = time.strftime("%I:%M%p")

        schedule = load_schedule(file_path)

        if current_time in schedule and current_time not in triggered:
            text = schedule[current_time]

            threading.Thread(target=alert, args=(text,), daemon=True).start()
            threading.Thread(target=speak, args=(text,), daemon=True).start()

            triggered.add(current_time)

        time.sleep(10)
