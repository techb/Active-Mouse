import ctypes
import time

print("Mouse is active every 10 minutes. Closing this window will stop active_mouse.exe")
while True:
    ctypes.windll.user32.SetCursorPos(200,200)
    time.sleep(600)
    ctypes.windll.user32.SetCursorPos(100,100)
    time.sleep(600)