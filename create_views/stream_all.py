import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@localhost:15984/')
print couch
db = couch[sys.argv[1]]
print db
view = ViewDefinition('category', 'all', 
'''function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
doc.metadata.place.name == 'Sydney')

var hour = new Date(doc.metadata.created_at).getHours();
var date = new Date(doc.metadata.created_at).toString();
if(constraint_1)  
emit([doc.metadata.place.name,'all',doc._id,doc.metadata.coordinates.coordinates,date], 1); 
}''')
view.sync(db)

view = ViewDefinition('category', 'morning_text', 
'''function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
doc.metadata.place.name == 'Sydney')

var hour = new Date(doc.metadata.created_at).getHours();
var date = new Date(doc.metadata.created_at).toString();
constraint_2 = (hour >=4) && (hour <=9)

if(constraint_1 && constraint_2)  
emit([doc.metadata.place.name,'morning',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1); 
}''')

view.sync(db)

view = ViewDefinition('category', 'night_text', 
'''function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
doc.metadata.place.name == 'Sydney')

var hour = new Date(doc.metadata.created_at).getHours();
var date = new Date(doc.metadata.created_at).toString();
constraint_2 = (hour >=21) || (hour <=2)

if(constraint_1 && constraint_2)  
emit([doc.metadata.place.name,'night',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1); 
}''')

view.sync(db)

print 'complete!'
