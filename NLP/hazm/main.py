# coding=utf-8
from __future__ import unicode_literals

from hazm import *

normalizer = Normalizer()
normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند')
'اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند'

sent_tokenize('ما هم برای وصل کردن آمدیم! ولی برای پردازش، جدا بهتر نیست؟')
word_tokenize('ولی برای پردازش، جدا بهتر نیست؟')

stemmer = Stemmer()
stemmer.stem('کتاب‌ها')
'کتاب'
lemmatizer = Lemmatizer()
lemmatizer.lemmatize('می‌روم')
'رفت#رو'

tagger = POSTagger(model='resources/postagger.model')
tagger.tag(word_tokenize('ما بسیار کتاب می‌خوانیم'))

chunker = Chunker(model='resources/chunker.model')
tagged = tagger.tag(word_tokenize('کتاب خواندن را دوست داریم'))
tree2brackets(chunker.parse(tagged))

parser = DependencyParser(tagger=tagger, lemmatizer=lemmatizer)
parser.parse(word_tokenize('زنگ‌ها برای که به صدا درمی‌آید؟'))
