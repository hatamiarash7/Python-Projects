# -*- coding: utf-8 -*
import Tkinter as tk
import threading
import ttk
import warnings

import MySQLdb

from helper import News


class Database:
    def __init__(self):
        self.DB = MySQLdb.connect("localhost", "ir_system", "ir1234", "ir_system")
        warnings.filterwarnings('ignore', category=MySQLdb.Warning)
        self.progress = 0
        self.progress_var = tk.DoubleVar()
        self.popup = self.progress_bar = None

    @staticmethod
    def start():
        db = MySQLdb.connect("localhost", "ir_system", "ir1234", "ir_system")
        cursor = db.cursor()
        try:
            cursor.execute("DROP TABLE IF EXISTS NEWS")
            sql = """CREATE TABLE IF NOT EXISTS NEWS (
                     ID  INT PRIMARY KEY NOT NULL,
                     TITLE  TEXT NULL ,
                     BODY LONGTEXT NULL ,
                     DATE VARCHAR(11) NULL,
                     TIME VARCHAR(8) NULL,
                     TOPICS TEXT NULL
                     )"""
            cursor.execute(sql)
            cursor.execute("DROP TABLE IF EXISTS TOKENS")
            sql = """CREATE TABLE IF NOT EXISTS TOKENS (
                                 ID INT PRIMARY KEY NOT NULL ,
                                 DID INT NOT NULL,
                                 TOKEN VARCHAR(25) NOT NULL,
                                 TF INT NULL,
                                 DF INT NULL 
                                 )"""
            cursor.execute(sql)
            db.close()
        except Warning as a_warning:
            pass
        return True

    def add(self, id, title, body, date, time, topics):
        cursor = self.DB.cursor()
        if id and title and body:
            title = title.replace("'", "''")
            body = body.replace("'", "''")
            sql = "INSERT INTO NEWS(ID, TITLE, BODY, DATE, TIME, TOPICS) VALUES ('%s','%s','%s','%s','%s','%s')"
            try:
                cursor.execute(sql % (id, title, body, date, time, topics))
                self.DB.commit()
                return 0
            except MySQLdb.Error, e:
                self.DB.rollback()
                print id,
                print e
                return 1
        else:
            return 0

    def add_token(self, tokens):
        add_thread = threading.Thread(target=self.threadAddManyToken, args=(tokens,))
        add_thread.start()

        self.popup = tk.Toplevel()
        self.popup.wm_attributes('-type', 'splash')
        tk.Label(self.popup, text="Token being added ...").grid(row=0, column=0)
        self.progress_bar = ttk.Progressbar(self.popup, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=1, column=0)
        self.popup.pack_slaves()

    @staticmethod
    def read():
        db = MySQLdb.connect("127.0.0.1", "ir_system", "ir1234", "ir_system")
        cursor = db.cursor()
        sql = """SELECT * FROM NEWS"""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            news = []
            for row in results:
                news.append(News(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                ))
            db.close()
            return news
        except:
            db.close()
            return False

    @staticmethod
    def get_index(element, list_element):
        try:
            index_element = list_element.index(element)
            return index_element
        except ValueError:
            return None

    def threadAddToken(self, tokens):
        cursor = self.DB.cursor()
        i = 0
        index = 1
        step = float(100.0 / len(tokens))
        print "There is " + str(len(tokens)) + " token !!"
        for token in tokens:
            sql = "INSERT INTO TOKENS(ID, DID, TOKEN) VALUES ('%s','%s','%s')"
            try:
                # cursor.execute(sql % (self.get_index(token, tokens), str(token.get_id()), token.get_token()))
                t = token.get_token().replace("'", "''")
                cursor.execute(sql % (index, str(token.get_id()), t))
                self.DB.commit()
                index += 1
            except MySQLdb.Error, e:
                self.DB.rollback()
                i += 1
                print str(token.get_id()) + " " + token.get_token()
                print e
            self.popup.update()
            self.progress += step
            self.progress_var.set(self.progress)
        self.popup.destroy()
        self.DB.close()
        return i

    def threadAddManyToken(self, tokens):
        cursor = self.DB.cursor()
        # sql = "SET GLOBAL max_allowed_packet=600*1024*1024"
        # cursor.execute(sql)
        i = 0
        try:
            params = [(str(item.get_id()), item.get_token().replace("'", "''")) for item in tokens if
                      len(item.get_token().replace("'", "''")) < 20]
            sql = """INSERT INTO TOKENS(DID, TOKEN) VALUES (%s, %s);"""
            cursor.executemany(sql, params)
            self.DB.commit()
            print "\a"
        except MySQLdb.Error, e:
            print "Error : ",
            print e
            self.DB.rollback()
            i += 1
        self.popup.destroy()
        self.DB.close()
        return
