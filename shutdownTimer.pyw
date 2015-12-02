import os
from time import sleep, time, localtime
from Tkinter import *

root = Tk()
root.wm_title('Shutdown timer')

hour = StringVar()
hour.set('h')
hours = Entry(root, width=5, textvariable=hour)
hours.pack(side=LEFT)

minute = StringVar()
minute.set('m')
minutes = Entry(root, width=5, textvariable=minute)
minutes.pack(side=LEFT)

second = StringVar()
second.set('s')
seconds = Entry(root, width=5, textvariable=second)
seconds.pack(side=LEFT)

def set_timer(*args):
    h = int(hours.get())
    m = int(minutes.get())
    s = int(seconds.get())
    while s >= 60:
        s = s-60
        m = m+1
    while m >= 60:
        m = m-60
        h = h+1
    sec = 3600*h + 60*m + s

    time_left = StringVar()
    time_left_field = Entry(root, width=7, textvariable=time_left)
    time_left_field.pack(side=LEFT)

    t_end = time() + sec
    end_date = localtime(t_end)
    end_date_string = '  {:02d}:{:02d}:{:02d}    {}/{:02d}/{:02d}'.format(
        end_date[3], end_date[4], end_date[5], end_date[0], end_date[1],
        end_date[2])
    date_label = Label(root, text=end_date_string)
    date_label.pack(side=LEFT)
    
    while t_end - time() > 0:
        sec = int(t_end - time())
        time_left.set(sec)

        h = sec/3600
        sec = sec%3600
        m = sec/60
        sec = sec%60
        s=sec

        second.set(s)
        minute.set(m)
        hour.set(h)

        root.update()
        sleep(1)
    os.system('shutdown -s -f')

def Quit(*args):
    root.destroy()

root.bind('<Return>', set_timer)
root.bind('<Escape>', Quit)

root.mainloop()
