# -*- coding: utf-8 -*
from itertools import chain
from lxml import etree

from lxml.etree import tostring

import db as database
import helper


class Reader:
    def __init__(self):
        pass

    @staticmethod
    def read():
        doc = etree.parse('reut2-001.sgm', etree.XMLParser(encoding='UTF-8', ns_clean=True, recover=True))
        root = doc.getroot()
        reuters = root.getchildren()
        counter = 0
        news = []
        print "Reading News ... ",
        for content in reuters:
            if content.get('TOPICS') == "YES":
                counter += 1
                DATE_STRING = content.findtext("DATE")
                ID = content.get("NEWID")
                TITLE = BODY = TOPICS = ""
                for c in content:
                    if c.tag == "TEXT":
                        TITLE = c.findtext("TITLE")
                        BODY = c.findtext("BODY")
                    if c.tag == "TOPICS":
                        parts = ([c.text] +
                                 list(chain(*([c.text, tostring(c), c.tail] for c in c.getchildren()))) +
                                 [c.tail])
                        TOPICS += ''.join(filter(None, parts))
                TOPICS = TOPICS.replace("<D>", ",").replace("</D>", ",")[:-2]
                F = list(set(TOPICS.split(',')))
                FINAL_TOPICS = ""
                for i in range(len(F)):
                    FINAL_TOPICS += F[i] + ','
                FINAL_TOPICS = FINAL_TOPICS[:-1]
                news.append(helper.News(
                    ID,
                    TITLE,
                    BODY,
                    DATE_STRING.split()[0],
                    DATE_STRING.split()[1].split('.')[0],
                    FINAL_TOPICS
                ))

        print "OK !"
        print "Check DB ... ",
        db = database.Database()
        if not db.start():
            print "ERROR !"
        else:
            print "OK !"
            print "Add To Database ... ",
            cc = 0
            for new in news:
                cc += db.add(
                    new.get_id(),
                    new.get_title(),
                    new.get_body(),
                    new.get_date(),
                    new.get_time(),
                    new.get_topics()
                )
            if cc == 0:
                print "OK !"
            else:
                print "ERROR !"
            db.DB.close()
