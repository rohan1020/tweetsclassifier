import config
from pymongo import MongoClient

def getCollection(name):

  client = MongoClient()

  client = MongoClient('localhost', 27017)
  db = client[config.DB_NAME]

  return db[name]



