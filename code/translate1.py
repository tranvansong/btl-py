import os
import time
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import googletrans
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from os import path
from pydub import AudioSegment
from PyPDF2 import PdfFileReader


root = Tk()
root.title("Phần mềm dịch ngôn ngữ pro")
root.geometry("1080x500")
root.resizable(False, False)
root.configure(background="white")

def label_change():
    b1 = box1.get()
    b2 = box2.get()
    label1.configure(text=b1)
    label2.configure(text=b2)
    
    root.after(100, label_change) # sau 0.1s thi doi

#translate text

def translate_now():
    try:
        t = text1.get(1.0,END)
        trans = Translator()
        trans1 = trans.translate(text=t, src=box1.get(), dest=box2.get())
        text2.delete(1.0,END)
        text2.insert(END, trans1.text)
    except:
        open_popup()

#open popup error
def open_popup():
   top= Toplevel(root)
   top.geometry("600x250")
   top.title("Error")
   Label(top, text= "Bạn chưa chọn ngôn ngữ", font=('Roboto 18 bold')).place(x=150,y=80)


def speak_text1():
    t = text1.get(1.0, END)
    v = box1.get()
    print(t)
    languagekey = languageKeys[list(language.values()).index(v.lower())]
    print(languagekey)
    myobj = gTTS(t,lang=languagekey,slow=False)
    myobj.save("test1.mp3")
    playsound("test1.mp3")
    os.remove("test1.mp3")

def speak_text2():
    t = text2.get(1.0, END)
    v = box2.get()
    print(t)
    languagekey = languageKeys[list(language.values()).index(v.lower())]
    print(languagekey)
    myobj = gTTS(t,lang=languagekey,slow=False)
    myobj.save("test2.mp3")
    playsound("test2.mp3")
    os.remove("test2.mp3")


#open file text
def open_file():
    tf = filedialog.askopenfilename(initialdir="C:/", title="Open file", filetypes=(("Text Files", "*.txt"),))
    tf = open(tf, 'r')
    print(tf.name)
    data = tf.read()
    text1.delete(1.0, END)
    text1.insert(END, data)
    tf.close()

#open file pdf
def pdf_trans():
    pdf_file = filedialog.askopenfilename(initialdir="C:/Desktop", title= "Open your pdf file", filetypes=(("PDF Files", "*.pdf"),))
    
    reader = PdfFileReader(pdf_file)
    num_pages = reader.numPages
    
    total_text = ""
    
    for p in range(num_pages):
        page = reader.getPage(p)
        pdf_text_page = page.extract_text()
        total_text = total_text + pdf_text_page 
    text1.delete(1.0, END)
    text1.insert(END, total_text)

#upload file audio
def upload_file_audio():
    tf = filedialog.askopenfilename(initialdir="C:/", title="Open file", filetypes=(("Audio Files", "*.mp3"),))
    tf = open(tf, 'r')
    sound = AudioSegment.from_mp3(tf.name)
    sound.export("img_and_test/transcript.wav", format="wav")


# transcribe audio file                                                         
    AUDIO_FILE = "img_and_test/transcript.wav"
    s = ""                                       
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        s+=r.recognize_google(audio)
    print(s)
    text1.delete(1.0, END)
    text1.insert(END, s)
    tf.close()


icon_img = PhotoImage(file = "img_and_test/icon.png")
root.iconphoto(False, icon_img)

language = googletrans.LANGUAGES
languageList = list(map(lambda x: x.title(), language.values())) # list languages in the world
languageKeys = list(language.keys()) # list key of countries


# left part
box1 = ttk.Combobox(root, values=languageList, font="Arial 15", state="r")
box1.place(x = 140, y = 50)
box1.set("English")

label1 = Label(root, text="English", font="Arial 30 bold", bg="white", width=16, bd=5, relief="groove")
label1.place(x = 60, y = 100)


# right part
box2 = ttk.Combobox(root, values=languageList, font="Arial 15", state="r")
box2.place(x = 680, y = 50)
box2.set("Select language")

label2 = Label(root, text="Select language", font="Arial 30 bold", bg="white", width=16, bd=5, relief="groove")
label2.place(x = 600, y = 100)


# first frame
f1 = Frame(root, bg="white", bd=2)
f1.place(x=60,y=180,width=395,height=204)

text1 = Text(f1,font="Arial 16", bg="white", relief="groove", wrap="word", border=3, padx=6, pady=5)
text1.place(x=0,y=0,width=385,height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# speaker button 1
speaker1_icon = PhotoImage(file="img_and_test/speaker.png")
photoimage1 = speaker1_icon.subsample(10, 10)
speaker1 = Button(root, text = "", image = photoimage1, compound = LEFT, cursor="hand2", command=speak_text1)
speaker1.place(x=60, y=385)


# second frame
f2 = Frame(root, bg="white", bd=2)
f2.place(x=600,y=180,width=395,height=204)

text2 = Text(f2,font="Arial 16", bg="white", relief="groove", wrap="word", border=3, padx=6, pady=5)
text2.place(x=0,y=0,width=385,height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#speaker button 2
speaker2_icon = PhotoImage(file="img_and_test/speaker.png")
photoimage2 = speaker2_icon.subsample(10, 10)
speaker2 = Button(root, text = "", image = photoimage2, compound = LEFT, cursor="hand2", command=speak_text2)
speaker2.place(x=600, y=385)


# translate button
translate = Button(root, text="Translate", font=("Arial", 16), activebackground="white",cursor="hand2", bd=1, width=10, height=2, bg="black",fg="white",command=translate_now)
translate.place(x=460, y = 250)

label_change()

# open_file text button
open_file_text = Button(root, text="Upload file text to translate", font=("Roboto", 12), cursor="hand2", padx=5, pady=5, command=open_file)
open_file_text.place(x=110, y=385)

# upload file audio button
upload_file_audio_va = Button(root, text="Upload file audio(.mp3)", font=("Roboto", 12), cursor="hand2", padx=5, pady=5, command=upload_file_audio)
upload_file_audio_va.place(x = 60, y = 430)

#open file pdf button
open_pdf = Button(root, text = "Choose pdf file to translate", font = ("Roboto", 12), cursor="hand2", padx=5, pady=5, command=pdf_trans)
open_pdf.place(x = 320, y = 385)

# loop 
root.mainloop()