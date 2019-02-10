import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
 r.adjust_for_ambient_noise(source)
 print ("speak:  ")
 audio = r.listen(source)

 try:

     text = r.recognize_google(audio)
     print ("You said: {}".format(text))
 except:
     pint("Voice not recognized")
