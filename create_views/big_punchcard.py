import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@localhost:15984/')
print couch
db = couch[sys.argv[1]]
print db
view = ViewDefinition('punchcard', 'punchcard', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')

var hour = new Date(doc.metadata.json.created_at).getHours();
var day = new Date(doc.metadata.json.created_at).getDay();
var date = new Date(doc.metadata.json.created_at).toString();
 
if(constraint_1)  
emit([doc.metadata.json.place.name,day,hour,date], 1); 
}

''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)


print 'complete!'
