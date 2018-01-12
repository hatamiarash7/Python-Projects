# -*- coding: utf-8 -*
from nltk.stem import PorterStemmer

import helper
import logging
import time


class Process:
    def __init__(self):
        self.news = None
        self.titles = self.res_titles = []
        self.bodies = self.res_bodies = []
        self.stopwords = []
        self.stemmed = []

    def tokenize(self, news):
        logging.info("Tokenizing ...")
        print "Tokenize ... "
        self.news = news
        for topic in news:
            titles = topic.get_title().split()
            for title in titles:
                self.titles.append(helper.Token(topic.get_id(), title.lower()))
            bodies = topic.get_body().split()
            for body in bodies:
                self.bodies.append(helper.Token(topic.get_id(), body.lower()))

    def remove_stopwords(self):
        print "StopWords ... "
        self.stopwords = self.stop_words()
        self.res_titles = [token for token in self.titles if token.get_token() not in self.stopwords]
        self.res_bodies = [token for token in self.bodies if token.get_token() not in self.stopwords]

    def stemming(self):
        print "Stemming ... "
        ps = PorterStemmer()
        for token in self.res_titles:
            self.stemmed.append(helper.Token(token.get_id(), ps.stem(token.get_token())))
        for token in self.res_bodies:
            self.stemmed.append(helper.Token(token.get_id(), ps.stem(token.get_token())))

    @staticmethod
    def stop_words():
        with open("stopwords.txt") as file:
            stopwords = [l.strip() for l in file]
        return stopwords

    def get_stemmed(self):
        return self.stemmed
