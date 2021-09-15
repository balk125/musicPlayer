from tkinter import *
from tkinter import filedialog
from os import chdir,listdir,system
from time import sleep
from pygame import mixer

master = Tk()

volume = 10
i = 0

chdir(f'D:\MUSIC')
list1=(listdir()) # YOU CAN ALSO WRITE AS list1=(listdir('D:\MUSIC'))
dict1={i:f"{list1[i]}" for i in range(len(list1))}

message = dict1[i]

def music_on_loop(file,):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.set_volume(volume / 10)

def play():

    while True:
        try:
            global i
            music_on_loop(dict1[i])
            message_bar(Name_level)
            
        except Exception as e:
            i = i + 1
            continue
        else:
            break;


def next_song():
    global i
    i = i + 1
    message_bar(Name_level)

    while True:
        try:
            music_on_loop(dict1[i])
        except Exception as e:
            i = i + 1
            continue
        else:
            break

def previous_song():
    global i
    if i!=0:
        i = i - 1
    else:
        i=0
    while TRUE:
        try:
            music_on_loop(dict1[i])
            message_bar(Name_level)
        except Exception as e:
            i = i + 1
            continue
        else:
            break
        
def message_bar(Name_level):
    global i
    message = dict1[i]
    Name_level.config(text=str(message))

    



master.title("Kanhaiya Music player")
widget_width = 640
windget_lenght = 420
master.maxsize(widget_width,windget_lenght)
master.minsize(widget_width-100,windget_lenght-80)
master.geometry(f'{widget_width}x{windget_lenght}')

f1=Frame(master,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
# label=Label()

Name_level = Label(master,fg=("#ff3300"), text="Now Playing", font="comicsansms 15 bold")
Name_level.pack(side=TOP, anchor='nw')


# PLay_entry = Entry(master, textvariable="kanhaiay",font="comicsansms 15",width=40,borderwidth=2)
# PLay_entry.pack(side=TOP, anchor='nw')

#buttons=------------------------------------

play_button = Button(master, text="Play",fg="blue",bg="yellow" ,width=2, height=1,font="verdana 15 bold",padx=30,command=play)
play_button.config()
play_button.pack(side=LEFT,padx=5)

next_button = Button(master, text="Next", fg="blue", bg="yellow", width=2, height=1, font="verdana 15 bold", padx=30,command=next_song).pack(side=LEFT,padx=5)

previous_button = Button(master, text="Previous", fg="blue", bg="yellow", width=2, height=1, font="verdana 15 bold", padx=30,command=previous_song).pack(side=LEFT,padx=5)
exit_button = Button(master, text="Exit", fg="blue", bg="yellow", width=2, height=1, font="verdana 15 bold", padx=30, command=master.destroy).pack(side=LEFT,padx=5)

suffle_button = Checkbutton(master, text="Suffle", fg="blue",width=2, height=1, font="verdana 15 bold", padx=30).pack(side=LEFT)



master.mainloop()