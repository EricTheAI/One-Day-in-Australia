# [Team 2]
# Posung Chen / poc2 / 773278
# Xiao liang / liangx4 / 754282
# Jiawei Zhang / jiaweiz6 / 815546
# Jia Wang / jiaw8 / 815814
# Fan Hong / hongf / 795265

#Sydney

import time,tweepy
import json,math
from pip._vendor import requests
from textblob import TextBlob


consumer_key = "YKeO06yZg9Lwzef1HpuYomB3o"
consumer_secret = "VgGmkmeM7Ju2h6IMLpjSB8BJcyeJPtj59UM3hJjJ4pKYMqrNT8"
access_token = "440654863-V15Pefn5Hc8WD2oLdrT4B0Fmd7MJpeRv97oUoXBh"
access_secret = "tffVMDbLyavkqktvyypWlrRxshQ9l5lOE0MDRr4xZpKp7"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

while True:
    try:
        start_time = time.time()
        text_each_iteration = api.search(count="100",geocode="-33.8489611,151.2887468,50km")
    #     with open("rest_syd.json","a+") as f:
        for line in text_each_iteration["statuses"]:
            json_str = json.dumps(line)
    #         f.write("%s\n" % json_str)
            id = str(line['id'])
    #         print id
    #             print json_str
            blob_text = str(TextBlob(line['text']).sentiment.polarity)
    #         print blob_text
            r=requests.put("http://localhost:5984/rest/"+id,data='{"category":"sydney","metadata":'+json_str+',"sentiment":'+blob_text+'}')            
    except tweepy.TweepError:  
        print "wait"
        used_time = time.time() - start_time
        start_time = time.time()
        time.sleep(math.ceil(60 * 15+1-used_time))

