# -*- coding: utf-8 -*
import ScrolledText
import Tkinter as tk
import logging
import threading
import ttk
from Tkinter import *
from lxml import etree

import db
import notification
import parse as parser
import process as Processor
import tkn


class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)


class Example(Frame):
    def __init__(self, **kw):
        Frame.__init__(self, **kw)
        self.initUI()
        self.res = None
        self.title = self.body = None
        self.progress = 0
        self.progress_var = tk.DoubleVar()
        self.popup = self.progress_bar = None
        self.logger = None

    def initUI(self):
        self.master.title("Reuters IR System")
        self.pack(fill=BOTH, expand=True)

        b = Button(self, text="Parse", width=8, command=self.onClick_Parse)
        b.place(x=20, y=20)

        b = Button(self, text="Load", width=8, command=self.onClick_Load)
        b.place(x=120, y=20)

        b = Button(self, text="Process", width=8, command=self.onClick_Process)
        b.place(x=220, y=20)

        st = ScrolledText.ScrolledText(self, width=190, height=9, state='disabled')
        st.configure(font='TkFixedFont')
        st.place(x=0, y=539)

        text_handler = TextHandler(st)

        # Logging configuration
        logging.basicConfig(filename='test.log',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Add the handler to logger
        self.logger = logging.getLogger()

        self.logger.addHandler(text_handler)

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
        logging.info("Load News ...")
        d = db.Database()
        self.res = d.read()
        if not self.res:
            notification_manager = notification.Notification_Manager(background="white")
            notification_manager.alert("ERROR !!")
        else:
            listbox = Listbox(self, width=40, height=29)
            listbox.place(x=20, y=70)
            listbox.bind('<<ListboxSelect>>', self.onClick_ListBox)
            scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=listbox.yview)
            scrollbar.pack(side="right", fill="y")
            listbox.config(yscrollcommand=scrollbar.set)
            for new in self.res:
                listbox.insert(END, str(new.get_id()) + '|' + new.get_title())
            self.title = Label(self, text="Select From List ...")
            self.title.place(x=380, y=70)
            self.body = Label(self, text="...")
            self.body.place(x=380, y=110)

    def onClick_Process(self):
        process = Processor.Process()
        process.tokenize(self.res)
        logging.info("Remove StopWords ...")
        process.remove_stopwords()
        logging.info("Stemming ...")
        process.stemming()
        stemmed = process.get_stemmed()
        logging.info("Add Tokens To DB ...")
        # print "Add Tokens ..."
        # d = db.Database()
        # d.add_token(stemmed)
        print "Calculate Frequencies ... \a"
        process.frequency()


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
        logging.info("Check Database ... ")
        print "Check Database ... ",
        if d.start():
            print "OK !"
        else:
            print "ERROR !"
        for i in range(0, 22):
            index = 'reut2-' + '{:03}'.format(i) + '.sgm'
            logging.info("Open File : " + index + " ... ")
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
        print
        print "Parsed !!"
        logging.info("Parsed !!")
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


def callback():
    print "called the callback!"


def main():
    root = Tk()
    width = 1366
    height = 600
    x = (root.winfo_screenwidth() - width) / 2
    y = (root.winfo_screenheight() - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    app = Example()
    menu = tk.Menu()
    root.configure(menu=menu)

    help_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About Me", command=callback)

    root.mainloop()


if __name__ == '__main__':
    main()
