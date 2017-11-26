# -*- coding: utf-8 -*
import warnings

import MySQLdb

from helper import News


class Database:
    def __init__(self):
        self.DB = MySQLdb.connect("localhost", "ir_system", "ir1234", "ir_system")
        warnings.filterwarnings('ignore', category=MySQLdb.Warning)

    @staticmethod
    def start():
        db = MySQLdb.connect("localhost", "ir_system", "ir1234", "ir_system")
        cursor = db.cursor()
        try:
            cursor.execute("DROP TABLE IF EXISTS NEWS")
            sql = """CREATE TABLE IF NOT EXISTS NEWS (
                     ID  INT PRIMARY KEY NOT NULL,
                     TITLE  TEXT,
                     BODY LONGTEXT,
                     DATE VARCHAR(11),
                     TIME VARCHAR(8),
                     TOPICS TEXT
                     )"""
            cursor.execute(sql)

            cursor.execute("DROP TABLE IF EXISTS TOKENS")
            sql = """CREATE TABLE IF NOT EXISTS TOKENS (
                                 ID  INT PRIMARY KEY NOT NULL,
                                 TOKEN  TEXT,
                                 TF INT,
                                 DF INT
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

    def add_token(self, list):

    @staticmethod
    def read():
        db = MySQLdb.connect("localhost", "ir_system", "ir1234", "ir_system")
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
