from tkinter import *
import requests
import json
import win32com.client as wc

root = Tk()
root.title("Audio Dictionary!")
root.geometry("400x380")

def SearchInfo():
    value = entry.get()
    api_key = f"https://api.dictionaryapi.dev/api/v2/entries/en/{value}"
    api_req = requests.get(api_key)
    api_dict = json.loads(api_req.text)
    
    definitions = []
    for meaning in api_dict[0]['meanings']:
        for definition in meaning['definitions']:
            definitions.append(definition['definition'])

    text.insert("1.0",definitions[0])    

def SpeakInfo(text):
    speaker = wc.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


search_icon = PhotoImage(file="C:/Users/hp/Desktop/More/PYTHON/PYTHON PROJECTS/Tkinter Projects/search.png")
speak_icon = PhotoImage(file="C:/Users/hp/Desktop/More/PYTHON/PYTHON PROJECTS/Tkinter Projects/speaker.png")
text_label = Label(root,text="Audio Dictionary",font=('impact',30))
text_label.pack(pady=20)

frame = Frame(root)
frame.pack()

entry = Entry(frame,width=25,font=("Comic Sans MS", 12,'bold'),bd=5)
entry.grid(row=0, column=0)

search_button = Button(frame,image=search_icon,padx=10,bg="lightgreen",command=SearchInfo)
search_button.grid(row=0,column=1)

speak_button = Button(frame,image=speak_icon,text=" Speak Aloud",compound=LEFT,bd=3,bg="white",command=lambda:SpeakInfo(text.get("1.0",END)))
speak_button.grid(row=1,column=0)

text = Text(root,bg="light yellow",font=("Times new roman",10),height=10,width=60,padx=10,pady=30,fg="purple")
text.pack()

root.mainloop()
