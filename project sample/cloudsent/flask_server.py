import json
import couchdb
from flask import Flask, jsonify, render_template
from textblob import TextBlob

# flask  settings
app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/v1/sentiment/<message>')
def sentiment(message):
    # couchdb settings
    server = couchdb.client.Server('http://localhost:5984/')
    db = server['twitter_users']
    list = db.view('_design/default/_view/'+message)
    response = []
    for r in list:
        text = r.key
        text = TextBlob(text)
        response.append({'polarity' : str(text.polarity) , 'subjectivity' : str(text.subjectivity), 'date' : r.value})    
    return json.dumps(response)

@app.route('/api/v1/graph/<message>')
def graph(message):
    # couchdb settings
    server = couchdb.client.Server('http://localhost:5984/')
    db = server['twitter_users']
    list = db.view('_design/default/_view/'+message)
    response = []
    for r in list:
        print(r.value);
        text = r.key
        text = TextBlob(text)
        response.append({'location' : r.value})    
    return json.dumps(response)

##################################################################
# NEW DEVELOPMENT                                                #
##################################################################

# RAW VIEW - Get Particular tweet
@app.route('/rawtweet/<tweetid>')
def rawtweet(tweetid):
    # DB configuration
    server = couchdb.client.Server('http://localhost:5984/')
    database = server['twitter']  # Using a smaller db for testing
    results = database.get(tweetid)
    return results


# TEMPLATES VIEW - Get particular tweet - NOT USING
@app.route('/viewtweet/<tweetid>')
def viewtweet(tweetid):
#results = database.get(tweetid)
#if results['analytics']['sentiment'] == 'positive' :
#    return render.result_pos(results)
#elif results['analytics']['sentiment'] == 'negative' :
#    return render.result_neg(results)
#else :
#    return render_template('result.html', tweetid=tweetid)

# 404 NOT FOUND
@app.errorhandler(404)
def page_not_found(error):
    return "404 NOT FOUND : Your Request cannot be reached"

##################################################################
# END                                                            #
##################################################################


 
if __name__ == "__main__":
    app.run(debug=True)
