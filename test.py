from gtts import gTTS
import googletrans
from googletrans import Translator
from playsound import playsound
# print(googletrans.LANGUAGES)
translator = Translator()
res = translator.translate("Tôi 20 tuổi") # translate from vi to en
print(res.text)
  
# The text that you want to convert to audio
mytext = res.text
# Language in which you want to convert
language = res.dest # language = en

print(res.dest)
print(googletrans.LANGUAGES)
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("test.mp3")
playsound("test.mp3")