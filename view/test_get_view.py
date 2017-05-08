import couchdb
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
db = couch['cloud2']

design_doc = view.get_doc(db)
print design_doc
