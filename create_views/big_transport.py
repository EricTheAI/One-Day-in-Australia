#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch[sys.argv[1]]
print db
view = ViewDefinition('category', 'transport', 
'''
function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')

regex=/(#| |^)(tram)( |$)|\uD83D\uDE8B|\uD83D\uDE8A/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'tram',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(train|rail|metro)( |$)|\uD83D\uDE86|\uD83D\uDE89|\uD83D\uDE87/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'train',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(taxi)( |$)|\uD83D\uDE95|\uD83D\uDE96/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'taxi',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(bus)( |$)|\uD83D\uDE8C|\uD83D\uDE8D|\uD83D\uDE8F/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'bus',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(walk|walking)( |$|s|es|ed)|\uD83D\uDEB6/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'walk',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(bike|bicycle|biking|bicycling|s|es|ed|d)( |$)|\uD83D\uDEB4|\uD83D\uDEB5\u200D/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'bike',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(drive|driving)( |$|s|es|ed|d)|\uD83D\uDE97|\uD83D\uDE98/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'car',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(airplane|plane)( |$)|\u2708|\uD83D\uDEE9|\uD83D\uDEEB|\uD83D\uDEEC/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'plane',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(ferry|ferries)( |$)|\u26F4/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'airplane',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(light rail)( |$)|\uD83D\uDE88/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'light rail',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

regex=/(#| |^)(uber)( |$|s|es|ed)/i
constraint_2 = doc.metadata.json.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,'uber',doc._id,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at], 1); 

}
''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

print 'complete!'
