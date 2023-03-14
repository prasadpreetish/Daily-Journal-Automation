import time
import pyautogui
from datetime import date

time.sleep(2)
print("Welcome to DayLee Desktop App !")
time.sleep(1)
today = str(date.today().strftime("%d %B"))
data = []
numOfTasks = int(input("Please tell me How many tasks did you do today ?? "))
print("What's the " +str(numOfTasks)+ " things you have done today ! ")
if numOfTasks<0:
    print("Please enter atleast one task")
else:
    if numOfTasks==1:
        data.append(input("Please enter the only task you did today : "))
    else: 
        counter = 1
        data.append(input("Enter the first task you did: "))
        while counter!=(numOfTasks-1):
            time.sleep(1)
            data.append(input("Enter the next task you have done : "))
            counter+=1
        time.sleep(1)
        data.append(input("Enter the last tasks you did : "))
        time.sleep(1)
author = input("Please enter the sailor of this ship : ")
print("Wish you best of Luck !")
time.sleep(1)
pyautogui.press("win")
pyautogui.write("notepad")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("Hey these are the notes for the day of "+today)
time.sleep(2)
pyautogui.press("enter")
for i in range(len(data)):
    pyautogui.write(data[i])
    pyautogui.press("enter")
    time.sleep(1)
time.sleep(1)
pyautogui.hotkey("ctrl","s")
time.sleep(2)
pyautogui.write(""+today+" notes by "+author)
time.sleep(1)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("alt","f4")
pyautogui.hotkey("alt","f4")
pyautogui.hotkey("alt","f4")
pyautogui.hotkey("alt","f4")