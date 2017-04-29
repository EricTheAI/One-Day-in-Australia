#!/usr/bin/env python
#
# Twitter state machine sampler.
# Full spec handles crawl by city OR user.
# Currently we finalize with only city.
# 'Boston, MA' place ID: 67b98f17fdcf20be
#

from __future__ import print_function
import time
import sys
import os
import tweepy
import json
import couchdb
import textblob

# Harvest mode: ('CITY', 'USERS')
HARVEST_MODE = os.environ['TWITTER_HARVEST_MODE']
PLACE_ID = '67b98f17fdcf20be'
MAX_TWEETS_PER_SEARCH = 100
DB_NAME = 'twitter'

AUTHS = [
    {
        'consumer_key': 'VMAXFU1xfYWo8fXeCZlG8FlLq',
        'consumer_secret': 'GBUtcNEGtxY8qTkd6jErKI70PBAdIDdUyWZwXg1H6QE7KtbKV4',
        'access_key': '3180647443-XiL3H0Yxt3qPq7J2HgyzQGLsBhK7CWAnj3etVgW',
        'access_token_secret': 'uD1J2MH7RvQ4MRLrYDlSAc999wHnI8jsPmeK5WHBLG0ky'
    },
    {
        'consumer_key': 'RWG77BWeRymf1FoFWIKZjigli',
        'consumer_secret': 'TDyQCxKxB9o5zxIe9WCQETy3Paw8T57DuBB772SA5WZYqOIUSL',
        'access_key': '22651013-tL49l2oBX7ooochixyuzkTqhJBbJbq2oVrDSuEYlB',
        'access_token_secret': 'oZojkB9n9RP0hf4cfgdVoDT7bHZKbtTkavVPTJxSXxgHr'
    },
    {
        'consumer_key': 'oWSXynBYeAu6VavSXsPYqwVag',
        'consumer_secret': 'myi810lDxEMsdrx44icHt2UYI9Dkw8kFjcGqW7XpEbyrPx8hNy',
        'access_key': '3180509622-3ZK2X0pqPz2X96mJuIK5Xpd5PBlEzfNdmpmQTig',
        'access_token_secret': '8zgxTMoABJ80pfJm88ISsQsxUKpdb6JGbH8th0cXGOmKj'
    },
    {
        'consumer_key': '8w5xQbiWoLlC9eNYAZt6qBb3i',
        'consumer_secret': 'L4h4ArOMalcdIYEg62QAWVHSLe75RiaxApZzYjelMjjmd3dXtG',
        'access_key': '580647653-1MLL52CT6mwBpviA9irw7wgz0z23J3F7wG8Dra1J',
        'access_token_secret': '1bC7wFvhDHYg6SKiQKrwDkT5sKmgHPg8UCHzuf6MnNclk'
    },
    {
        'consumer_key': 'U7as5rmAHX28zgkamOQgg',
        'consumer_secret': 'Cn5suk7F7bBKQyugzwvnzlsvnpfwNG7udioc9FZoc',
        'access_key': '1462235833-uIS1Wd4NdFOn8H5YmarfS9K400WMBU6uI4rszS0',
        'access_token_secret': 'g7bQjeiUwoF6B5hlWluTsHO2wv1CYoDgFsaTPwu8l1w'
    }
]


def log(*objs):
    """ Print to log. """
    print(*objs, file=sys.stderr)

def sentiment_analyze_text(tweet_text):
    """ Returns sentiment analysis for text. """
    tweet_analysis = textblob.TextBlob(tweet_text)
    if tweet_analysis.sentiment.polarity < 0:
        sentiment = "negative"
    elif tweet_analysis.sentiment.polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "positive"

    results = {
        "polarity": tweet_analysis.sentiment.polarity,
        "subjectivity": tweet_analysis.sentiment.subjectivity,
        "sentiment": sentiment
    }
    return results

def connect_twitter():
    """ Connects to Twitter and returns API wrappers. """
    apis = []
    for cred in AUTHS:
        auth = tweepy.OAuthHandler(cred['consumer_key'], cred['consumer_secret'])
        auth.set_access_token(cred['access_key'], cred['access_token_secret'])
        api = tweepy.API(
            auth_handler=auth,
            parser=tweepy.parsers.JSONParser()
        )
        apis.append(api)
    return apis

def harvest_city(apis, db):
    since_id = 0
    largest_id = 0
    max_id = -1
    smallest_id = -1

    # Harvest forever
    api_index = 0
    while True:
        try:
            # Get wrapper
            api = apis[api_index]
            # Update api_index for next wrapper in round-robin fashion
            api_index = (api_index + 1) % len(apis)
            # Kickstart search
            if max_id == -1:
                log('New search')
                response = api.search(
                    q='place:{}'.format(PLACE_ID),
                    count=MAX_TWEETS_PER_SEARCH,
                    since_id=str(since_id),
                    result_type='recent'
                )
            # Continue search
            else:
                response = api.search(
                    q='place:{}'.format(PLACE_ID),
                    count=MAX_TWEETS_PER_SEARCH,
                    result_type='recent',
                    since_id=str(since_id),
                    max_id=str(max_id)
                )
        except tweepy.TweepError:
            log('Hit rate limit: sleeping')
            time.sleep(60 * 15)
            continue
        except Exception as e:
            # Exception occurred, sleep for 3 seconds
            log(e)
            time.sleep(3)
            continue

        # If tweet list is empty, we've hit the end.
        if len(response['statuses']) == 0:
            log('Tweet list is empty')

            # Sleep for 5 minutes
            time.sleep(60 * 5)

            # Update next search configuration
            since_id = largest_id
            max_id = -1

            # Restart
            continue

        for tweet in response['statuses']:
            # Provide '_id' for CouchDB
            tweet['_id'] = tweet['id_str']
            
            # Update stats
            if smallest_id == -1:
                smallest_id = tweet['id']
            else:
                smallest_id = min(smallest_id, tweet['id'])
            largest_id = max(largest_id, tweet['id'])

            # Analyze text
            sentiment = sentiment_analyze_text(tweet['text'])
            tweet['analytics'] = sentiment

            # Save to CouchDB
            try:
                db.save(tweet)
            except Exception as e:
                # Write out exception and ignore
                log(e)
                pass
        
        # Update next search configuration
        max_id = smallest_id - 1

def harvest_users(apis, db):
    while True:
        # Do nothing
        # TODO: Complete later if required.
        log('Not doing anything, sleeping for 15 minutes')
        time.sleep(60 * 15)

def get_twitter_couchdb(db_name):
    server = couchdb.Server()
    try:
        log('{} creating'.format(db_name))
        db = server.create(db_name)
    except Exception as e:
        log('{} already exists'.format(db_name))
        pass

    db = server[db_name]
    return db

def main():
    # Connect to Twitter
    log('Connecting to Twitter')
    apis = connect_twitter()

    # Connect to CouchDB
    log('Connecting to CouchDB')
    db = get_twitter_couchdb(DB_NAME)

    # Harvest
    if HARVEST_MODE == 'CITY':
        harvest_city(apis, db)
    elif HARVEST_MODE == 'USERS':
        harvest_users(apis, db)
    else:
        raise Exception('Invalid HARVEST_MODE {}'.format(HARVEST_MODE))


if __name__ == '__main__':
    main()
