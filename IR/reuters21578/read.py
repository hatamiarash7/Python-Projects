# -*- coding: utf-8 -*
import MySQLdb
from lxml import etree

db = MySQLdb.connect("185.105.186.135", "root", "3920512197", "hyper_online")

doc = etree.parse('reut2-001.sgm', etree.XMLParser(encoding='UTF-8', ns_clean=True, recover=True))
root = doc.getroot()
reuters = root.getchildren()
counter = 0
for content in reuters:
    if content.get('TOPICS') == "YES":
        counter += 1
    for c in content:
        if c.tag == "TEXT":
            print "title : ",
            print c.findtext('TITLE')
            print
            print "body : ",
            print c.findtext('BODY')
    print
print counter
