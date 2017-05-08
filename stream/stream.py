from tweepy import OAuthHandler
import json,tweepy
from pip._vendor import requests
from textblob import TextBlob


consumer_key = 'gwSo8FuaZkoRyinoCEEyKDJPi'
consumer_secret = 'KIQSPgKNL3oZji1vtoMsZhE9SENQ3mWwSxOMtf7xC1qBAINirs'
access_token = '853210075980218368-GJ5nvNrRKU0yl0Yl4ZQ51LAvDXY1YMl'
access_secret = 'vBDtOIb5ZI6sDB7zO2rmevJrvK1GxFuH8Z5RuW6AZYLKr'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

class StreamListener_todb(tweepy.StreamListener):

    def on_status(self, status):
        json_str = json.dumps(status._json)
        id = str(status._json['id'])
        blob_text = str(TextBlob(status._json['text']).sentiment.polarity)
        r=requests.put("http://localhost:5984/stream/"+id,data='{"category":"australia","metadata":'+json_str+',"sentiment":'+blob_text+'}')

    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener_todb()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

stream.filter(locations=[109.5993213654,-44.55159558,159.3459911346,-11.059461736])
