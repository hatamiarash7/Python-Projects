# -*- coding: utf-8 -*
import Tkinter as tk
import threading
import ttk
from Tkinter import *
from lxml import etree

import db
import notification
import parse as parser
import process as Processor
import tkn


class Example(Frame):
    def __init__(self, **kw):
        Frame.__init__(self, **kw)
        self.initUI()
        self.res = None
        self.title = self.body = None
        self.progress = 0
        self.progress_var = tk.DoubleVar()
        self.popup = self.progress_bar = None

    def initUI(self):
        self.master.title("Reuters IR System")
        self.pack(fill=BOTH, expand=True)

        b = Button(self, text="Parse", width=8, command=self.onClick_Parse)
        b.place(x=20, y=20)

        b = Button(self, text="Load", width=8, command=self.onClick_Load)
        b.place(x=120, y=20)

        b = Button(self, text="Process", width=8, command=self.onClick_Process)
        b.place(x=220, y=20)

    def onClick_Parse(self):
        parse_thread = threading.Thread(target=self.threadParse)
        parse_thread.start()

        self.popup = tk.Toplevel()
        self.popup.wm_attributes('-type', 'splash')
        tk.Label(self.popup, text="Files being parsed ...").grid(row=0, column=0)
        self.progress_bar = ttk.Progressbar(self.popup, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=1, column=0)
        self.popup.pack_slaves()

    def onClick_Load(self):
        d = db.Database()
        self.res = d.read()
        if not self.res:
            notification_manager = notification.Notification_Manager(background="white")
            notification_manager.alert("ERROR !!")
        else:
            listbox = Listbox(self, width=40, height=27)
            listbox.place(x=20, y=70)
            listbox.bind('<<ListboxSelect>>', self.onClick_ListBox)
            scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=listbox.yview)
            scrollbar.pack(side="right", fill="y")
            listbox.config(yscrollcommand=scrollbar.set)
            for new in self.res:
                listbox.insert(END, str(new.get_id()) + '|' + new.get_title())
            self.title = Label(self, text="Select From List ...")
            self.title.place(x=380, y=20)
            self.body = Label(self, text="...")
            self.body.place(x=380, y=60)

    def onClick_Process(self):
        process = Processor.Process()
        process.tokenize(self.res)
        process.remove_stopwords()
        process.stemming()
        print str(process.get_stemmed()[250].get_id()) + ":" + process.get_stemmed()[250].get_token()

    def onClick_ListBox(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        id = value.split('|')[0]
        for new in self.res:
            if id == str(new.get_id()):
                self.title.config(text=new.get_title())
                self.body.config(text=new.get_body())

    def threadParse(self):
        reader = parser.Parser()
        d = db.Database()
        print "Check Database ... ",
        if d.start():
            print "OK !"
        else:
            print "ERROR !"
        for i in range(0, 22):
            index = 'reut2-' + '{:03}'.format(i) + '.sgm'
            print "Open File : " + index + " ... ",
            try:
                doc = etree.parse(index, etree.XMLParser(encoding='UTF-8', ns_clean=True, recover=True))
                print "OK !"
                reader.parse(doc)
            except:
                print "ERROR !"
            print
            self.popup.update()
            self.progress += 4.54
            self.progress_var.set(self.progress)
        self.popup.destroy()
        print('\a')
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
