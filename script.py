import pyautogui
import time
def position():
    direction = currentMouseX,currentMouseY  = pyautogui.position()
    #move = pyautogui.moveTo(32,41)
    # pyautogui.click('Jeremy')
    print(direction)
def terminal():
    pyautogui.hotkey('ctrl','alt','t')
    time.sleep(3)
    pyautogui.hotkey('alt','f10')

def exterm():
    pyautogui.write('exit')
    pyautogui.hotkey('enter')

def youtube():
    pyautogui.hotkey('ctrl','alt','t')
    time.sleep(3)
    pyautogui.hotkey('alt','f10')
    pyautogui.write('firefox')
    pyautogui.hotkey('enter')
    time.sleep(15)
    pyautogui.hotkey('alt','f10')
    time.sleep(5)
    pyautogui.hotkey('ctrl','t')
    time.sleep(3)
    pyautogui.moveTo(340,425)
    pyautogui.click()
    

def fav():
    pyautogui.moveTo(367,186)
    pyautogui.click()
    pyautogui.write('Na tum jano na hum')
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.moveTo(282,376)
    time.sleep(7)
    pyautogui.click()
    pyautogui.click()
    time.sleep(6)
    # pyautogui.hotkey('spacebar')

def fullscreen():
    pyautogui.hotkey('alt','f10')

def closingapp():
   move =  pyautogui.moveTo(10,39)
   pyautogui.click()

def click():
    pyautogui.click()

def resume():
    pyautogui.hotkey('k')


def down():
    pyautogui.hotkey('down')

    pass

def facebook():
    pyautogui.hotkey('ctrl','alt','t')
    time.sleep(3)
    pyautogui.hotkey('alt','f10')
    pyautogui.write('firefox')
    pyautogui.hotkey('enter')
    time.sleep(15)
    pyautogui.hotkey('alt','f10')
    time.sleep(5)
    pyautogui.hotkey('ctrl','t')
    time.sleep(3)
    pyautogui.moveTo(214,422)
    pyautogui.click()


position()