import config
import mongoconn
import nltk

coll = mongoconn.getCollection("tweets")

txt = list(coll.find())[3]['text']

tokens = nltk.word_tokenize(txt)
tagged = nltk.pos_tag(tokens)
print txt
print tagged

