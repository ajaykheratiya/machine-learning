Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import threading
from PIL import Image,ImageTk

bot = ChatBot("My Bot")
conversation = [
    "",
    "Hi",
    "Hola",
    "Good Morning",
    "Hello",
    "How you doin'?",
    "I'm doing great.",
    "That is good to hear.",
    "Thank you.",
    "You're welcome.",
    "Your name please...",
    "My name is Robot2.0",
    "Bye.",
    "Time to go now.",
    "Bye and have a nice day !!",
]
trainer = ListTrainer(bot)
trainer.train(conversation)
win = Tk()
win.geometry("600x620")
win.title("Chat Bot")

image = Image.open("abc.jpg")
photo = ImageTk.PhotoImage(image)
bot_label = Label(image=photo)
bot_label.pack()


def ask():
    query = textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    print(type(answer))
    msgs.insert(END, "Bot : " + str(answer))
    textF.delete(0, END)
    msgs.yview(END)
frame = Frame(win)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF = Entry(win, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(win, text="Ask", font=("Verdana", 20), command=ask)
btn.pack()
def enter_function(event):
    btn.invoke()
win.bind('<Return>', enter_function)
def repeatL():
    while True:
        takeQuery()
t = threading.Thread(target=repeatL)
t.start()
win.mainloop()

