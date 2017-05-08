import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@localhost:15984/')
print couch
db = couch[sys.argv[1]]
print db
print 'complete!'