import pyautogui

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')

def seek_forward():
    pyautogui.press('right')

def seek_backward():
    pyautogui.press('left')

def seek_forward_10s():
    pyautogui.press('l')

def seek_backward_10s():
    pyautogui.press('j')

def seek_backward_frame():
    pyautogui.press(',')

def seek_forward_frame():
    pyautogui.press('.')

def seek_to_beginning():
    pyautogui.press('home')

def seek_to_end():
    pyautogui.press('end')

def seek_to_previous_chapter():
    pyautogui.hotkey('ctrl', 'left')

def seek_to_next_chapter():
    pyautogui.hotkey('ctrl', 'right')

def decrease_playback_speed():
    pyautogui.hotkey('shift', ',')

def increase_playback_speed():
    pyautogui.hotkey('shift', '.')

def move_to_next_video():
    pyautogui.hotkey('shift', 'n')

def move_to_previous_video():
    pyautogui.hotkey('shift', 'p')


# ------------- Command Handler -------------
def perform_media_action(text):
    text = text.lower()

    if "volume up" in text or "awaaz badhao" in text:
        volume_up()

    elif "volume down" in text or "awaaz kam karo" in text:
        volume_down()

    elif "forward" in text or "aage badhao" in text:
        seek_forward()

    elif "backward" in text or "peeche le jao" in text:
        seek_backward()

    elif "forward 10" in text or "10 second aage chalo" in text:
        seek_forward_10s()

    elif "backward 10" in text or "10 second peeche chalo" in text:
        seek_backward_10s()

    elif "next frame" in text or "aage ka frame" in text:
        seek_forward_frame()

    elif "previous frame" in text or "peeche ka frame" in text:
        seek_backward_frame()

    elif "beginning" in text or "starting se" in text:
        seek_to_beginning()

    elif "end" in text or "khatam tak" in text:
        seek_to_end()

    elif "previous chapter" in text or "pichla chapter" in text:
        seek_to_previous_chapter()

    elif "next chapter" in text or "agla chapter" in text:
        seek_to_next_chapter()

    elif "slow down" in text or "speed kam karo" in text:
        decrease_playback_speed()

    elif "speed up" in text or "speed badhao" in text:
        increase_playback_speed()

    elif "next video" in text or "agla video" in text:
        move_to_next_video()

    elif "previous video" in text or "pichla video" in text:
        move_to_previous_video()

    else:
        pass 



