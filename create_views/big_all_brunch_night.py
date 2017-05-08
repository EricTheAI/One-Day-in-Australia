import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch[sys.argv[1]]
print db
view = ViewDefinition('category', 'all', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
if(constraint_1) 
emit([doc.metadata.json.place.name,'all',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 
}''')
view.sync(db)

#2.brunch
view = ViewDefinition('category', 'brunch',
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')

regex=/(#| |^)brunch( |$|s|es)/i
constraint_2 = doc.metadata.json.text.match(regex)
var hour = new Date(doc.metadata.json.created_at).getHours();
constraint_3 = (hour >=9) && (hour <=15)

if(constraint_1 && constraint_2 && constraint_3) 
emit([doc.metadata.json.place.name,'brunch',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 
}''')
view.sync(db)

#3.nightout
view = ViewDefinition('category', 'nightout', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')

regex=/(#| |^)(bar|clubbing|beer|cocktail|wine|sake|champagne|vodka|tequilla|cheers)( |$|s|es)|\uD83C\uDF7A|\uD83C\uDF78|\uD83C\uDF77|\uD83C\uDF76|\uD83C\uDF79|\uD83C\uDF7B|\uD83C\uDF7E/i
constraint_2 = doc.metadata.json.text.match(regex)

var hour = new Date(doc.metadata.json.created_at).getHours();
constraint_3 = (hour >=18) || (hour <=9)

if(constraint_1 && constraint_2 && constraint_3)  
emit([doc.metadata.json.place.name,'nightout',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 
}''')
view.sync(db)

print 'complete!'
