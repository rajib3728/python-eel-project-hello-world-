import eel
import pyautogui
import time
@eel.expose
def hello(x):
    s=0
    a=x.split(":")
    t=int(a[0])*60+int(a[1])
    while(1):
        time.sleep(1)
        s=s+1
        if s//2==t:
            break
        else:
            pyautogui.press('volumeup')#incrase volume
            pyautogui.press('volumeup')#incrase volume
            pyautogui.press('volumeup')#incrase volume
            pyautogui.press('volumeup')#incrase volume
            pyautogui.press('volumeup')#incrase volume
            pyautogui.press('volumeup')#incrase volume
            pyautogui.press('volumedown')#decrease volume
            pyautogui.press('volumedown')#decrease volume
            pyautogui.press('volumedown')#decrease volume
            pyautogui.press('volumedown')#decrease volume
            pyautogui.press('volumedown')#decrease volume
            pyautogui.press('volumedown')#decrease volume
                     
eel.init("web")

eel.start("index.html",size=(1600,900))