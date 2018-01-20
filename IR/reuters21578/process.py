# -*- coding: utf-8 -*
import logging

import toolz
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
        print "Tokenize ...\a"
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
        print "StopWords ...\a"
        self.stopwords = self.stop_words()
        self.res_titles = [token for token in self.titles if token.get_token() not in self.stopwords]
        self.res_bodies = [token for token in self.bodies if token.get_token() not in self.stopwords]

    def stemming(self):
        print "Stemming ...\a"
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

    def frequency(self):
        self.merged = self.titles + self.bodies
        '''
        print "merge : " + str(len(self.merged))
        print "merge : " + str(sum(1 for _ in unique_words))
        print "news : " + str(len(self.news))
        
        len(merged) = 1,589,828
        len(unique) = 73,528
        len(news) = 11,097
        '''
        unique_words = toolz.unique(self.merged, key=lambda word: word.token)

        DF = open('DF.txt', 'wb')
        TF = open('TF.txt', 'wb')
        CF = open('CF.txt', 'wb')
        DF.write("{: >15} {: >20} {: >15}\n\n".format('ID', 'TOKEN', 'DF'))
        TF.write("{: >15} {: >20} {: >15}\n\n".format('ID', 'TOKEN', 'TF per DF'))
        CF.write("{: >15} {: >20} {: >15}\n\n".format('ID', 'TOKEN', 'CF'))

        i = 0
        for token in unique_words:
            tf_list = ""
            i += 1
            frequency = 0
            for topic in self.news:
                temp = topic.get_title().split() + topic.get_body().split()
                count = temp.count(token.get_token())
                if count > 0:
                    frequency += 1
                    token.inc_tf_by(count)
                    tf_list += str(topic.get_id()) + ':' + str(count) + ' '
            if frequency != 0:
                token.set_df(frequency)
                print str(i)
                DF.write("{: >15} {: >20} {: >15}\n".format(str(i), token.get_token(), str(token.get_df())))
                TF.write("{: >15} {: >20}          {}\n".format(str(i), token.get_token(), tf_list))
                CF.write("{: >15} {: >20} {: >15}\n".format(str(i), token.get_token(), str(token.get_tf())))
