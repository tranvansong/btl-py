import os
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
from gtts import gTTS
from playsound import playsound



root = Tk()
root.title("Phan mem dich ngon ngu")
root.geometry("1080x500")
root.resizable(False, False)
root.configure(background="white")

def label_change():
    b1 = box1.get()
    b2 = box2.get()
    label1.configure(text=b1)
    label2.configure(text=b2)
    
    root.after(100, label_change) # sau 0.1s thi doi


def translate_now():
    t = text1.get(1.0,END)
    trans = Translator()
    trans1 = trans.translate(text=t, src=box1.get(), dest=box2.get())
    text2.delete(1.0,END)
    text2.insert(END, trans1.text)


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


icon_img = PhotoImage(file = "icon.png")
root.iconphoto(False, icon_img)

# change_img = PhotoImage(file = "change1.png")
# img_label = Label(root,image= change_img, width=100)
# img_label.place(x = 460, y = 100)

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
speaker1_icon = PhotoImage(file="speaker.png")
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
speaker2_icon = PhotoImage(file="speaker.png")
photoimage2 = speaker2_icon.subsample(10, 10)
speaker2 = Button(root, text = "", image = photoimage2, compound = LEFT, cursor="hand2", command=speak_text2)
speaker2.place(x=600, y=385)


# translate button
translate = Button(root, text="Translate", font=("Arial", 16), activebackground="white",cursor="hand2", bd=1, width=10, height=2, bg="black",fg="white",command=translate_now)
translate.place(x=460, y = 250)

label_change()

# loop 
root.mainloop()