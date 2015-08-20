import config
import mongoconn
import nltk

coll = mongoconn.getCollection("tweets")

allTweets = list(coll.find())

def getDataSet():

    out = [x['text'] for x in allTweets]
    return out

