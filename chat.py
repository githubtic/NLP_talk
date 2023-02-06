import os
import openai
import speech_recognition as sr
import pyttsx3
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
r = sr.Recognizer()
def set_language(language='fr'):
    engine.setProperty('language',language)
    return True

   
openai.organization = "org-h5VxbC88EYAQrQMOgMIiT9bL"
openai.api_key = "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"
SpeakText("Salut je suis votre robot que puis je faire pour vous?")
QUESTION="what is the temperature at wagadugu"
    

t=input('do you want to continue? \n- :')
while(t.lower()!='no'.lower()):   
    #SpeakText("que puis je faire d'autre pour vous?")
    #QUESTION=input("Salut je suis votre robot que puis je faire pour vous?\n -: ")
 
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2, language="fr-FR")
            MyText = MyText.lower()
 
            print("\nI eared: "+MyText+"\n")
            #SpeakText(MyText)
            reponse=openai.Completion.create(model="text-davinci-003",max_tokens=1000,prompt=MyText,temperature=0.6)
            SpeakText(reponse["choices"][0]["text"])
            print("\nRobot : "+reponse["choices"][0]["text"]+"\n")
            
     
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")
    t=input('do you want to continue? \n- :')
    