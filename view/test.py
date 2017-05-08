import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch[sys.argv[1]]
print db
