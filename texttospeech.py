from gtts import gTTS
import os
abc=open('sample.text')
text=nabc.read()
language = 'en'
obj = gTTS(text=text,lang=language,slow= flase)
object.save("sample.mp3")
obj.system("sample.mp3")
