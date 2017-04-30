import tweepy
from textblob import TextBlob

consumer_key = '847hKxaD1NzYzhBqC8bVnn5yL'
consumer_secret = '2y0CHV8xjnm9yzRbQPpPxTrdUMDESISloc2krIcdkTJ32H39Hi'

access_token = '4888721774-9TSHlOWSJsUuIkYdJBazTKGZuEw9NuhpSkOlI6I'
access_token_secret = '9w4ePSrDLZPS8028wdkoHNFyseue2ewwPD5CvpmuYyqQ1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print tweet.text
    analysis = TextBlob(tweet.text)
    print analysis.sentiment
    print '\n'
#     print sentence.sentiment.polarity
