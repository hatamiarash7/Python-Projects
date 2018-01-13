# -*- coding: utf-8 -*
import logging

from nltk.stem import PorterStemmer

import helper


class Process:
    def __init__(self):
        self.news = None
        self.titles = self.res_titles = []
        self.bodies = self.res_bodies = []
        self.stopwords = []
        self.stemmed = []
        self.merged = []

    def tokenize(self, news):
        logging.info("Tokenizing ...")
        print "Tokenize ... "
        self.news = news
        for topic in news:
            titles = topic.get_title().split()
            # TO-DO: convert to one line

            for title in titles:
                self.titles.append(helper.Token(topic.get_id(), title.lower()))

            bodies = topic.get_body().split()
            for body in bodies:
                self.bodies.append(helper.Token(topic.get_id(), body.lower()))

                # self.titles=[helper.Token(topic.get_id(), title.lower()) for title in titles if helper.Token(topic.get_id(), title.lower()) not in self.titles]
                # self.bodies=[helper.Token(topic.get_id(), body.lower()) for body in bodies if helper.Token(topic.get_id(), body.lower()) not in self.bodies]

        ''' 
        Logs :
        967850 with repeats
        '''

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
        with open("stopwords.txt") as words:
            stopwords = [l.strip() for l in words]
        return stopwords

    def get_stemmed(self):
        return self.stemmed

    def document_frequency(self):
        self.merged = self.titles + self.bodies
        '''
        len(merged) = 1,589,828
        len(news) = 11,097
        '''
        i = 0
        for token in self.merged:
            i += 1
            frequency = 0
            for topic in self.news:
                temp = topic.get_title().split() + topic.get_body().split()
                if temp.count(token.get_token()) > 0:
                    frequency += 1
            token.set_df(frequency)
            row = [str(i), token.get_token(), str(token.get_df())]
            print("{: >20} {: >20} {: >20}".format(*row))

            # for token in self.merged:
            #     docs = []
            #     if token.get_token() not in self.stopwords:
            #         for topic in self.news:
            #             temp = topic.get_title().split() + topic.get_body().split()
            #             # if temp.count(token.get_token()) > 0 and token.get_id() not in docs:
            #             if temp.count(token.get_token()) > 0 :
            #                 docs.append(str(token.get_id()))
            #         token.set_df(len(docs))
            #         print token.get_token() + " | " + str(token.get_df()) + " | " + str(docs)
