#!/usr/bin/env python
# Author: Willie Lawrence - cptx032@gmail.com
# You can use importing it or
# calling it by terminal
# To see the config commands type in terminal:
#     ./tknotify.py --help

import tkFont
from Tkinter import *


def print_help(i=0):
    __msg = """Usage:
  tknotify.py -t <title> [OPTION...]

Help Options:
  -h, --help			Show the help options

Application Options:
  -title			Title of notification
  -msg				Body message of notification
  -alpha			Transparency level of window
  -title			Title of notification
  -expire			Expire time of window (default: 2000ms)
  -spacing			Distance of window to screen NE corners (default: 20)
  -justify			Title and message text justification. ('left'|'right'|'center', default: 'left')
  -text_padding			Distance of text to window
"""
    print(__msg)
    sys.exit(i)


# [fixme] > icon
def show(**kws):
    """
    Attributes:
        title: the title message (in bold font)
        msg(opt):	the message
        expire_time(opt): how long the message will be showed (default 2000ms)
        spacing(opt): the distance to screen border (default 20)
        justify(opt): The title and msg justify (default 'left')
        text_padding(opt): The padding of title or msg (default 50)
        alpha(opt): The alpha of windows (default 1.0)
    """
    title = kws.get("title")
    msg = kws.get("msg", False)
    expire_time = kws.get("expire_time", 2000)
    spacing = kws.get("spacing", 20)
    justify = kws.get("justify", CENTER)
    text_padding = kws.get("text_padding", 50)
    alpha = kws.get("alpha", 1.0)

    top = Toplevel()
    top.attributes("-alpha", alpha)
    TITLE_FONT = tkFont.Font(size=9, family="TkDefaultFont", weight=tkFont.BOLD)
    MSG_FONT = tkFont.Font(size=9, family="TkDefaultFont")
    top.withdraw()
    top.attributes("-topmost", 1)
    top.overrideredirect(True)
    top.config(bd=0, highlightthickness=0, bg="#2a2a2a")
    Label(top, text=title, fg="#fff", bd=0,
          highlightthickness=0, justify=justify, font=TITLE_FONT,
          bg=top["bg"]).pack(expand=YES, fill=BOTH)
    if msg:
        Label(top, text=msg, fg="#fff", bd=0,
              highlightthickness=0, justify=justify, font=MSG_FONT,
              bg=top["bg"]).pack(expand=YES, fill=BOTH)
    top.update_idletasks()
    SW = top.winfo_screenwidth()  # screen width
    WW = TITLE_FONT.measure(title)
    if msg and MSG_FONT.measure(msg) > WW:
        WW = MSG_FONT.measure(msg)
    WW += text_padding
    qt_lines_title = len(title.split("\n"))
    WH = qt_lines_title * TITLE_FONT.metrics().get("ascent")
    WH += (qt_lines_title - 1) * TITLE_FONT.metrics().get("linespace")
    if WH < 50:
        WH = 50
    top.geometry("%dx%d+%d+%d" % (WW, WH, SW - WW - spacing, spacing))
    top.after(expire_time, top.destroy)
    top.deiconify()


def get_index(label):
    try:
        return sys.argv[sys.argv.index(label) + 1]
    except:
        pass
    return False


def notify(kws):
    a = Tk()
    a.withdraw()
    show(**kws)
    a.after(kws["expire_time"], a.destroy)  # root windows is doesn't destroyed
    a.mainloop()


if __name__ == "__main__":
    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        print_help()
    else:
        kws = {
            "title": get_index("-t") or print_help(),  # quits
            "msg": get_index("-msg"),
            "expire_time": int(get_index("-expire")) if get_index("-expire") else 2000,
            "spacing": int(get_index("-spacing")) if get_index("-spacing") else 20,
            "justify": get_index("-justify") or "left",
            "text_padding": int(get_index("-text_padding")) if get_index("-text_padding") else 50,
            "alpha": float(get_index("-alpha")) if get_index("-alpha") else 0.8
        }
        a = Tk()
        a.withdraw()
        show(**kws)
        a.after(kws["expire_time"], a.destroy)  # root windows is doesn't destroyed
        a.mainloop()
