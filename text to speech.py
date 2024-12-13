# Using gTTS (Google Text to Speech API):
# pip install gTTS

# from gtts import gTTS
# import os

# mytext = 'Welcome to geeksforgeeks!'
# language = 'en'
# myobj = gTTS(text=mytext, lang=language, slow=False)
# myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")


# Using pyttsx3 (Offline Text-to-Speech Library):
# pip install pyttsx3
# import pyttsx3
# text="hello, sudhanshu how are you"
# engine=pyttsx3.init()
# engine.say(text)
# engine.runAndWait()



import pyttsx3
engine=pyttsx3.init()
text=["sudhanshu","raushan","suman","santu","harsh","vishal","hrishikesh","function caching"]
text=["shoutout to "+x for x in text]
# new_list = []
# for x in text:
#   new_list.append(x+' word')
# my_list = new_list[:]
for txt in text:   
     engine.say(text)
     print(text)
     break
engine.runAndWait()

# for txt in text:
#      engine.say(f"shoutout to {txt}")
#      print(txt)
# engine.runAndWait()






# Changing Voice , Rate and Volume :

# import pyttsx3
# engine = pyttsx3.init() # object creation

# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()