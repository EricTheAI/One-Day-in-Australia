#Team 19: Boston by Omar El Samad (749907), Samuel Josei Jenkins (389975), Mubashir Munawar (713627), Xuan Fan (653226), Dinni Hayyati (666967)
from tweepy import StreamListener
from tweepy import Stream
import tweepy
import json
import couchdb
import datetime

#logs
logsfile = 'tweetsmininglogs.txt'

#Opening output file then printing time log
mylogsfile = open(logsfile, 'w')
mylogsfile.write('Job started on %s.\n' % (datetime.datetime.now()))

#Twitter credentials, keep private
CONSUMER_KEY = 'RWG77BWeRymf1FoFWIKZjigli'
CONSUMER_SECRET = 'TDyQCxKxB9o5zxIe9WCQETy3Paw8T57DuBB772SA5WZYqOIUSL'
ACCESS_TOKEN = '22651013-tL49l2oBX7ooochixyuzkTqhJBbJbq2oVrDSuEYlB'
ACCESS_TOKEN_SECRET = 'oZojkB9n9RP0hf4cfgdVoDT7bHZKbtTkavVPTJxSXxgHr'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#twitter db on couchdb
server = couchdb.Server()
try:
    db = server.create('twitter')
except:
    db = server['twitter']

#Streaming listerner
class StdOutListener(StreamListener):

    def on_data(self, data):
        # process stream data then insert to db
        tweetDoc = json.loads(data)
        try:
           #print(tweetDoc)
           tweetDoc["_id"] = str(tweetDoc['id'])
           MyCity = tweetDoc['place']['name']
           #Boston City only
           if MyCity == 'Boston':
              dbdoc = db.save(tweetDoc)
        except:
           print(tweetDoc["_id"], "Duplication occured")
           pass
        return True

    def on_error(self, status):
        print(status)
        mylogsfile.write('Error Status: %s %s.\n' % (status,datetime.datetime.now()))

if __name__ == '__main__':
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    #Boston city filteration
    #twitterStream.filter(locations=[-71.192,42.225,-70.994,42.422])
    twitterStream.filter(locations=[-72,42.5,-70,43.5])
