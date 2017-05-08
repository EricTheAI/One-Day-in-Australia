#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import couchdb
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch['cloud2']

#1.tweet time
view = ViewDefinition('coordinate', 'time', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
if(constraint_1) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates],doc.metadata.json.created_at); 
}''')
view.sync(db)

#2.brunch
view = ViewDefinition('coordinate', 'brunch',
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('brunch') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates],doc.metadata.json.text); 
}''')
view.sync(db)

#3.nightout
view = ViewDefinition('coordinate', 'nightout', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('bar') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('clubbing') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('beer') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('cocktail') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('wine') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('sake') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('champagne') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('vodka') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('tequilla') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF7A') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF78') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF77') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF76') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF79') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF7B') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('cheers') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF7E') != -1 

if(constraint_1 && constraint_2) 
emit([doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at],doc.metadata.json.text); 
}''')
view.sync(db)

print 'complete!'
