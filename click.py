#!/usr/bin/env python3
import subprocess,sys,time,os
def i(p):
 try:subprocess.check_call([sys.executable,'-m','pip','install',p,'--user'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 except:pass
try:import pyautogui
except:i('pyautogui');import pyautogui
print("Auto-clicker started. Ctrl+C to stop.")
try:
 while 1:pyautogui.click();print(f"Click {time.strftime('%H:%M:%S')}");time.sleep(5)
except:print("Stopped.")