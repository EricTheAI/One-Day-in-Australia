# melbourne

import time,tweepy
import json,math
from pip._vendor import requests
from textblob import TextBlob


consumer_key = "dfYT4JjSUWFdg6ngGXCQUKyX7"
consumer_secret = "GbCPNcQXaROQ10hb36yWAD41NGpLXPgiOjzv67APHLAlyHvYgU"
access_token = "788688840886059008-TQiojwHbQiT0HWTLISEALWmwwdIQ9S6"
access_secret = "vGAXyr1jXVkAzsWloE8Ab1xCohXF3fWCtJhn6wR5OfMUs"

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
            r=requests.put("http://localhost:5984/rest_melb/"+id,data='{"category":"melbourne","metadata":'+json_str+',"sentiment":'+blob_text+'}')            
    except tweepy.TweepError:  
        print "wait"
        used_time = time.time() - start_time
        start_time = time.time()
        time.sleep(math.ceil(60 * 15+1-used_time))
