# [Team 2]
# Posung Chen / poc2 / 773278
# Xiao liang / liangx4 / 754282
# Jiawei Zhang / jiaweiz6 / 815546
# Jia Wang / jiaw8 / 815814
# Fan Hong / hongf / 795265

# melbourne

import time,tweepy
import json,math
from pip._vendor import requests
from textblob import TextBlob


consumer_key = "k6EWfwg6Ndaek66TeVO6NnFOR"
consumer_secret = "DJW3HiATczarocY3EOvRMLCiRiL3J61I8SZypMubVhXYhst10m"
access_token = "858174767899189248-eG4y6ix2vWJMNC5ODHIq0iWYH8odrzg"
access_secret = "y5FnvgiVNUH94pJkh3kDCwyKnQpPFv9fPrURxEz1lbU0n"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

while True:
    try:
        start_time = time.time()
        text_each_iteration = api.search(count="100",geocode="-37.8141,144.9633,100km")
    #     with open("rest_melb.json","a+") as f:
        for line in text_each_iteration["statuses"]:
            json_str = json.dumps(line)
    #         f.write("%s\n" % json_str)
            id = str(line['id'])
#             print id
    #        print json_str
            blob_text = str(TextBlob(line['text']).sentiment.polarity)
    #         print blob_text
            r=requests.put("http://localhost:5984/rest/"+id,data='{"category":"melbourne","metadata":'+json_str+',"sentiment":'+blob_text+'}')            
    except tweepy.TweepError:  
        print "wait"
        used_time = time.time() - start_time
        start_time = time.time()
        time.sleep(math.ceil(60 * 15+1-used_time))


