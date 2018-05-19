# -*- coding: utf-8 -*-
import tkinter as tk
from datetime import datetime as dt
import winsound as wn
import time as t

master=tk.Tk()
master.geometry("150x250")

msghours=tk.StringVar()
entryhours=tk.Entry(master, textvariable=msghours)
entryhours.place(relx=.5, rely=.5, anchor="c")

msgmins = tk.StringVar()
entrymins = tk.Entry(master, textvariable=msgmins)
entrymins.place(relx=.5, rely=.9, anchor="c")

def funct_for_but(h, m):
    curr_t=str(dt.now().time())
    curr_h=int(curr_t[0:2])*3600
    curr_m=int(curr_t[3:5])*60
    need_h=h*3600
    need_m=m*60
    time_to_delay=need_h-curr_h+need_m-curr_m
    t.sleep(time_to_delay)
    for i in range(15):
        wn.PlaySound('meemintro.wav', wn.SND_ASYNC)
        t.sleep(1)
        wn.PlaySound('meemrage.wav', wn.SND_ASYNC)
        t.sleep(1)

button_send_data_to=tk.Button(master, text='ОТСЧЕТ', command=lambda : funct_for_but(int(str(entryhours.get())), int(str(entrymins.get()))))
button_send_data_to.pack()

master.mainloop()