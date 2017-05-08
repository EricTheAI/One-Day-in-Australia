import couchdb,json
from textblob import TextBlob
from pip._vendor import requests

r = requests.get("http://localhost:5984/cloud2/_design/Sent/_view/textView")
text_list = json.loads(r.text)
print "Get View!"

couch = couchdb.Server('http://admin:admin@localhost:5984/')
print couch
db = couch['cloud2']
print db

for tweet in text_list['rows']:
    doc = db.get(tweet['id'])
    doc['sentiment'] = TextBlob(tweet['value']).sentiment.polarity
    db.save(doc)
