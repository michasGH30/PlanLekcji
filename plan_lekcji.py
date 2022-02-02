from tkinter import *
from PIL import ImageTk, Image
from wakeonlan import send_magic_packet
from datetime import datetime
import socket
import subprocess
import os
import time
import requests
from bs4 import BeautifulSoup

host = '192.168.1.125'
port = 4005
# server=('192.168.1.120',4000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind((host, port))
day = datetime.today().weekday()
path = "D:/programowanie/python/app/"
nazwy = ["j.niem 2","#3","Aplik.deskt.-1/2","tworz.str-1/2","witryny i ap-1/2","j.ang 1-1/2","syst. baz da-1/2","wf-1/2","r_informat.-1/2","p.baz-1/2","wf-1/2"]
response = requests.get('http://zsz1.edu.pl/plan/plany/o8.html')

response.raise_for_status()

soup = BeautifulSoup(response.text,"html.parser")

lessons = [[0 for x in range(2)] for y in range(48)] 

table = soup.select('td[class="l"]')

res = []

for i in table:
    res.append(i)

for i in range(0,len(res)):
    b = res[i].select('span[class="p"]')
    for j in range(0,len(b)):
        a = b[j].get_text()
        c = a.split(">")[0]
        if c not in nazwy:
            lessons[i][j]=c

hours_end = [datetime(2001,6,30,8,45),datetime(2001,6,30,9,35),datetime(2001,6,30,10,25),
             datetime(2001,6,30,11,30),datetime(2001,6,30,12,25),datetime(2001,6,30,13,15),
             datetime(2001,6,30,14,5),datetime(2001,6,30,14,55)]
hours_st=[datetime(2001,6,30,8,0),datetime(2001,6,30,8,50),datetime(2001,6,30,9,40),
          datetime(2001,6,30,10,45),datetime(2001,6,30,11,40),datetime(2001,6,30,12,30),
          datetime(2001,6,30,13,20),datetime(2001,6,30,14,10)]


root = Tk()
root.title("Zarzadzanie i lekcje")
root.attributes("-fullscreen", True)
root.configure(background="white")
full = True


def raise_frame(frame):
    frame.tkraise()


f1 = Frame(root)
f1.grid(row=0, column=0, sticky="news")
f2 = Frame(root)
f2.grid(row=0, column=0, sticky="news")

f1.configure(background="white")
f2.configure(background="white")

b_down_img = Image.open(path + "b_down.png").resize((194, 239))
b_down_photo = ImageTk.PhotoImage(b_down_img)

b_up_img = Image.open(path + "b_up.png").resize((194, 239))
b_up_photo = ImageTk.PhotoImage(b_up_img)

sleep_img = Image.open(path + "sleep.png").resize((194, 239))
sleep_photo = ImageTk.PhotoImage(sleep_img)

sleep_dark_img = Image.open(path + "sleep_dark.png").resize((194, 239))
sleep_dark_photo = ImageTk.PhotoImage(sleep_dark_img)

fullscreen_img = Image.open(path + "fullscreen.png").resize((194, 239))
fullscreen_photo = ImageTk.PhotoImage(fullscreen_img)

fullscreen_light_img = Image.open(path + "fullscreen_light.png").resize((194, 239))
fullscreen_light_photo = ImageTk.PhotoImage(fullscreen_light_img)

power_img = Image.open(path + "power.png").resize((194, 239))
power_photo = ImageTk.PhotoImage(power_img)

power_light_img = Image.open(path + "power_light.png").resize((194, 239))
power_light_photo = ImageTk.PhotoImage(power_light_img)

vulcan_img = Image.open(path + "vulcan.png").resize((194, 239))
vulcan_photo = ImageTk.PhotoImage(vulcan_img)

def fullscreen():
    global full
    global fullscreen_button
    if full:
        root.attributes("-fullscreen", False)
        full = False
    elif not full:
        root.attributes("-fullscreen", True)
        full = True

def sleep():
    message = "sleep"
    # s.sendto(message.encode("utf-8"),server)
    raise_frame(f1)


def wake_up():
    for i in range(1, 1000):
        send_magic_packet("44-8A-5B-5C-80-C4")
    raise_frame(f2)


def shutdown_PC():
    message = "shutdown"
    # s.sendto(message.encode("utf-8"),server)
    raise_frame(f1)

def vulcan_open():
    pass

dark = False


def b_up():
    global power_button, fullscreen_button_f1, f1, f2,  c, t, light, permament_check, fullscreen_button, \
        shutdown_button, sleep_button, light_f2, permament_check_f2, l, n_l,vulcan_button
    global dark
    if not dark:
        dark = True
        light.configure(image=b_up_photo, bg="black")
        c.configure(bg="black", fg="white")
        t.configure(bg="black", fg="white")
        f1.configure(background="black")
        f2.configure(background="black")
        fullscreen_button_f1.configure(image=fullscreen_light_photo, bg="black")
        power_button.configure(image=power_light_photo, bg="black")
        permament_check.configure(bg="black", fg="white", selectcolor="black")
        fullscreen_button.configure(image=fullscreen_light_photo, bg="black")
        shutdown_button.configure(image=power_light_photo, bg="black")
        sleep_button.configure(image=sleep_dark_photo, bg="black")
        light_f2.configure(image=b_up_photo, bg="black")
        permament_check_f2.configure(bg="black", fg="white", selectcolor="black")
        l.configure(bg="black",fg="white")
        n_l.configure(bg="black",fg="white")
        vulcan_button.configure(bg="black")
    elif dark:
        dark = False
        light.configure(image=b_down_photo, bg="white")
        c.configure(bg="white", fg="black")
        t.configure(bg="white", fg="black")
        f1.configure(background="white")
        f2.configure(background="white")
        fullscreen_button_f1.configure(image=fullscreen_photo, bg="white")
        power_button.configure(image=power_photo, bg="white")
        permament_check.configure(bg="white", fg="black", selectcolor="white")
        fullscreen_button.configure(image=fullscreen_photo, bg="white")
        shutdown_button.configure(image=power_photo, bg="white")
        sleep_button.configure(image=sleep_photo, bg="white")
        light_f2.configure(image=b_down_photo, bg="white")
        permament_check_f2.configure(bg="white", fg="black", selectcolor="white")
        l.configure(bg="white",fg="black")
        n_l.configure(bg="white",fg="black")
        vulcan_button.configure(bg="white")


permament_var = IntVar()
lesson_string = StringVar()
next_lesson_string = StringVar()

light_f2 = Button(f2, text="UP", command=b_up, image=b_down_photo, bg="white")
light_f2.grid(row=0,column=0)
fullscreen_button = Button(f2, text="Fullscreen", command=fullscreen, image=fullscreen_photo, bg="white")
fullscreen_button.grid(row=0, column=2)
shutdown_button = Button(f2, text="Shutdown", command=shutdown_PC, image=power_photo, bg="white")
shutdown_button.grid(row=0, column=1)
sleep_button = Button(f2, text="Sleep", command=sleep, image=sleep_photo, bg="white")
sleep_button.grid(row=1, column=3)
permament_check_f2 = Checkbutton(f2, text="PERMAMENT", font=("Lato", 17), variable=permament_var, bg="white", fg="black")
permament_check_f2.grid(row=1, column=0)
l = Label(f2,textvariable=lesson_string,font=("Lato",23),bg="white")
l.grid(row=1, column = 1)
n_l = Label(f2,textvariable=next_lesson_string,font=("Lato",23),bg="white")
n_l.grid(row=1, column = 2)
vulcan_button = Button(f2,text="Vulcan",command=vulcan_open,image=vulcan_photo,bg="white")
vulcan_button.grid(row=0,column=3)

dt_string = StringVar()
time_string = StringVar()


power_button = Button(f1, text="Power", command=wake_up, image=power_photo, bg="white")
power_button.place(relx=0.5, rely=0, anchor=N)
fullscreen_button_f1 = Button(f1, text="Fullscreen", command=fullscreen, image=fullscreen_photo, bg="white")
fullscreen_button_f1.place(relx=1, rely=0, anchor=NE)
light = Button(f1, text="UP", command=b_up, image=b_down_photo, bg="white")
light.place(relx=0, rely=0, anchor=NW)
permament_check = Checkbutton(f1, text="PERMAMENT", font=("Lato", 17), variable=permament_var, bg="white", fg="black")
permament_check.place(relx=0, rely=0.65, anchor=W)
c = Label(f1, textvariable=dt_string, font=("Lato", 45), bg="white")
c.place(relx=0.5, rely=0.85, anchor=CENTER)
t = Label(f1, textvariable=time_string, font=("Lato", 80), bg="white")
t.place(relx=0.5, rely=0.65, anchor=CENTER)

now = datetime.now()
a = int(now.strftime("%H"))
n = datetime(2001,6,30,now.hour,now.minute)

dt_string.set(now.strftime("%d/%m/%Y"))
time_string.set(now.strftime("%H:%M:%S"))


def update():
    now = datetime.now()
    n = datetime(2001,6,30,now.hour,now.minute)
    count = 1
    for i in range(0,8):
        if hours_end[i] >= n >= hours_st[i]: 
            break
        else:
            count+=1
    c2 = 1
    if count == 9:
        for i in range(0,7):
            if hours_st[i+1] > n > hours_end[i]:
                break
            else:
                c2+=1
        d = (c2)*6 + day
        if d < len(lessons):
            if lessons[d][0] !=0:
                lesson_string.set("Lekcja:\n"+lessons[d][0])
            elif lessons[d][1] !=0:
                lesson_string.set("Lekcja:\n"+lessons[d][1])
        else:
            lesson_string.set("Nie masz lekcji")
    else:
        a = (count-1)*6 + day
        if lessons[a][0] !=0:
            lesson_string.set("Lekcja:\n"+lessons[a][0])
        elif lessons[a][1] !=0:
            lesson_string.set("Lekcja:\n"+lessons[a][1])
        else:
            lessin_string.set("Nie masz lekcji")
        b = count*6 + day
        if b < len(lessons):
            if lessons[b][0] !=0:
                next_lesson_string.set("Next lekcja:\n"+lessons[b][0])
            elif lessons[b][1] !=0:
                next_lesson_string.set("Next lekcja:\n"+lessons[b][1])
            else:
                next_lessin_string.set("Nie masz lekcji")
    dt_string.set(now.strftime("%d/%m/%Y"))
    time_string.set(now.strftime("%H:%M:%S"))
    global dark
    global permament_var
    var = permament_var.get()
    hour = int(now.strftime("%H"))
    if 5 <= hour <= 19 and var == 0:
        dark = True
        b_up()
    elif 5 >= hour >= 19 and var == 0:
        dark = False
        b_up()
    root.after(1000, update)


hostname = "192.168.1.127"
response = os.system('ping -c 1 ' + hostname)
if response == 0:
    raise_frame(f2)
else:
    raise_frame(f1)
root.after(1000, update)
root.mainloop()
