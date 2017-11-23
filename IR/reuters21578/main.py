from Tkinter import *

import db
import notification
import read as Reader
import tkn


class Example(Frame):
    def __init__(self, **kw):
        Frame.__init__(self, **kw)
        self.initUI()

    def initUI(self):
        self.master.title("Checkbutton")
        self.pack(fill=BOTH, expand=True)

        b = Button(self, text="Parse", width=8, command=self.onClick_Parse)
        b.place(x=20, y=20)

        b = Button(self, text="Load", width=8, command=self.onClick_Load)
        b.place(x=120, y=20)

        b = Button(self, text="Read", width=8, command=self.onClick_Read)
        b.place(x=220, y=20)

    def onClick_Parse(self):
        reader = Reader.Reader()
        reader.read()
        tkn.notify(
            kws={
                "title": "IR System",
                "msg": "Parsing Done",
                "expire_time": 2000,
                "spacing": 20,
                "justify": "left",
                "text_padding": 50,
                "alpha": 0.8
            }
        )

    def onClick_Load(self):
        d = db.Database()
        res = d.read()
        if not res:
            notification_manager = notification.Notification_Manager(background="white")
            notification_manager.alert("ERROR !!")
        else:
            listbox = Listbox(self, width=40, height=27)
            listbox.place(x=20, y=70)
            listbox.insert(END, "a list entry")
            listbox.bind('<<ListboxSelect>>', self.onClick_ListBox)
            for new in res:
                listbox.insert(END, str(new.get_id()) + '|' + new.get_title())

    def onClick_Read(self):
        pass

    def onClick_ListBox(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        id = value.split('|')[0]
        print id


def main():
    root = Tk()
    width = 1050
    height = 500
    x = (root.winfo_screenwidth() - width) / 2
    y = (root.winfo_screenheight() - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
