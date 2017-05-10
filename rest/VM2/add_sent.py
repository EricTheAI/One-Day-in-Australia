# [Team 2]
# Posung Chen / poc2 / 773278
# Xiao liang / liangx4 / 754282
# Jiawei Zhang / jiaweiz6 / 815546
# Jia Wang / jiaw8 / 815814
# Fan Hong / hongf / 795265

import couchdb,sys
from textblob import TextBlob
# from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@localhost:5987/')
db = couch[sys.argv[1]]


# map_fun = '''function(doc) {
#     emit([doc.metadata.text],null);
# }'''
results = db.view('DesignDoc/textView',keys=[sys.argv[2]])

# print len(results)
for result in results:
    doc = db.get(result.id)
    doc['sentiment'] = TextBlob(result.value).sentiment.polarity
    db.save(doc)

print 'complete!'
