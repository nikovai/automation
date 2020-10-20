import pyttsx3
import  speech_recognition as sr 
import os
import time
import script 
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.energy_thresold = 400
        r.adjust_for_ambient_noise(source, duration = 1)
        # speak('wait for 1 second let me understand your query')
        print('1 second')
        r.pause_thresold = 0
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        print(e)
        speak('say that again please')
        print('Say that again')
        return 'None'
    return query


if __name__ == '__main__':
    speak('Hello sir how can i help you')
    while True:
        query = command().lower()
        if 'hello'  in query:
            speak('hello how are you you')
            # new = command().lower()
        elif 'fine' in query:
            speak ('okay what you want from me')
            # query = command().lower()
        elif 'close' in query:
            speak('have a nice day am closing myself huhuhu')
            break
        elif 'terminal' in query:
            speak('opening mate terminal for you')

            script.terminal()
          
        elif 'shutdown' in query:
            speak('shutting down the system in 3 seconds')
            os.system('sudo shutdown now')
        elif 'exit'  in query:
            speak('closing the terminal')
    
            script.exterm()
        elif 'youtube' in query:
            speak('opening youtube sir')
            script.youtube()
            speak('do i have to search for your fav song sir')
            
        elif 'favourite' in query:
            speak('playing your favorite song enjoy')
            script.fav()
        
        elif 'full' in query:
            script.fullscreen()
        elif 'resume' in query:
            speak('song resumed')
            script.resume()
        elif 'out' in query:
            script.closingapp()

        elif 'play' in query:
            script.click()
            speak('playing sir')

        elif 'press' in query:
            script.click()
            speak('pressing sir')

        elif 'search' in query:
        # def search():
            import pyautogui
            pyautogui.moveTo(411,185)
            pyautogui.click()
            speak('which song you want to listen')
            new = command().lower()
            speak('searching {new} for you sir ')
            pyautogui.write(new)
            pyautogui.hotkey('enter')
            time.sleep(5)
            pyautogui.moveTo(282,376)
            pyautogui.click()
        elif "down" in query:
            speak("scrolling down sir")
            script.down()

        elif 'facebook' in query:
            speak('opening facebook sir')
            script.facebook()

        elif 'kill' in query:
            speak('which process you want to kill')
            proc = command().lower().replace(" ","")
            speak(f'killing {proc}')
            os.system(f'pidof {proc} > process.txt')
            with open('process.txt','r') as file:
                new =  file.read()
                
                os.system(f'kill  {new}')

                


