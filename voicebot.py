import pyttsx3 as p
import speech_recognition as sr

engine = p.init()

engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("Salam Aleykoum nanga def ?")

# def demo():
#     with sr.Microphone() as source:
#         r.energy_threshold = 10000
#         r.adjust_for_ambient_noise(source, 1.2)
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio, language="fr-FR")
#             print("Vous avez dit : {}".format(text))
#             speak("Vous avez dit : {}".format(text))
#         except:
#             print("Désolé, je n'ai pas compris !")
#             speak("Désolé, je n'ai pas compris !")

with sr.Microphone() as source:
    print("Waxxal daraa")
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "bonjour" or "salam" or "ça va" in text:
    speak("Je vais bien, Al Hamdoullilah")
else : 
    print("Désolé, je n'ai pas compris !")
    speak("Désolé, je n'ai pas compris !")
    
speak("Que puis-je faire pour vous ?")



