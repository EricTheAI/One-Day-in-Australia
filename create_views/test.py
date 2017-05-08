import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch[sys.argv[1]]
print db
#1.ski
view = ViewDefinition('tmp', 'gym', 
'''function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
doc.metadata.place.name == 'Sydney')
regex=/(#| |^)(gym)/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'gym',doc._id,doc.metadata.coordinates.coordinates,doc.metadata.created_at], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

print 'complete!'