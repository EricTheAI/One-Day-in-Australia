
#!/usr/bin/python
import web
import time
import tweepy
import json
import couchdb

# Templates
render = web.template.render('templates/')

# Url configure
urls = (
        "/","index",
        # Twitter related function
        "/twitter", "index",
        "/twitter/(.*)", "getTwitter",
        "/get_twitter/(.*)", "getTwitter",
        "/all/","getAll",
        # Sentiment related
        "/sentiment/", "developing",
        "/sentiment/negative", "getNegativeTweet",
        "/sentiment/positive", "getPositiveTweet",
        "/sentiment/netural", "getNeturalTweet",
        # User related function
        "/user" , "index",
        "/user/(.*)" , "user"
        )

# Database configure
couch = couchdb.Server()
db = couch['twitter']
usrDb = couch['twitter_users']

# Constant number

startIdx = 0
endIdx = 0

# Map function
def fun(doc):
    if doc['date']:
        yield doc['date'], doc

docs = '''function(doc) {
    emit(doc._id, null);
    }'''

usernames = '''function(doc) {
    if (doc.user) {
    emit(doc.user.screen_name, null);
    }
    }'''


# Main classes
class index:
    def GET(self):
        #i = web.input(name=None)
        return render.index()

# Get Twitter by ID
class getTwitter:
    def GET(self,docid):
        results = db.get(docid)
        if results['analytics']['sentiment'] == 'positive' :
            return render.result_pos(results)
        elif results['analytics']['sentiment'] == 'negative' :
            return render.result_neg(results)
        else :
            return render.result(results)

# Further functions developing
class Twitter:
    def GET(self):
        return None

# Get ALL twitter list  - Will be replaced by view
class getAll:
    def GET(self):
        counter = 0
        list = []
        db = couch['twitter2']  # Temp used smaller database
        for row in db.view('_all_docs'):
            if counter == 10 :
                break
            else :
                list.append(row)
                counter += 1
        return render.all(db)
    
    def POST(self):
        return None

# Sentiment related search - Developing
class getNegativeTweet:
    def GET(self):
        return None

class getPositiveTweet:
    def GET(self):
        return None

class getNeturalTweet:
    def GET(self):
        return None

# develop page
class developing:
    def GET(self):
        return render.developing()

# User related
class getUser:
    def GET(self):
        return None

# Def -  function parts
def get_tweets(self):
    return self.db.view('twitter/get_tweets')


# Views - Developing - Not used
def _create_views(self):
    count_map = 'function(doc) { emit(doc.id, 1); }'
    count_reduce = 'function(keys, values) { return sum(values); }'
    view = couchdb.design.ViewDefinition('twitter', 'count_tweets', count_map, reduce_fun=count_reduce)
    view.sync(self.db)
    
    get_tweets = 'function(doc) { emit(("0000000000000000000"+doc.id).slice(-19), doc); }'
    view = couchdb.design.ViewDefinition('twitter', 'get_tweets', get_tweets)
    view.sync(self.db)


def save_tweet(self, tw):
    tw['_id'] = tw['id_str']
    self.db.save(tw)

def count_tweets(self):
    for doc in self.db.view('twitter/count_tweets'):
        return doc.value



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

