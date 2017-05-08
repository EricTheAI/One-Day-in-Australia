#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import couchdb
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch['cloud2']

#1.junkfood
view = ViewDefinition('food', 'junk', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('kfc') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('maccas') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('mcdonald's') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('mcdonalds') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('hungryjack') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('hungry jack') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('fries') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('subway') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('chips') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('burger') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('combo') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('nugget') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('big mac') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('coke') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF54') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF5F') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF55') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('hot dog') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF2D') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#2.healthyfood
view = ViewDefinition('food', 'healthy', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('whole grain') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('whole-grain') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('wholegrain') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('fruit') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('melon') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('orange') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('apple') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('pear') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('grapes') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('banana') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('berries') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('protein powder') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('olive oil') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('celery') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('avocado') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('whole wheat') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('whole-wheat') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('wholewheat') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('almonds') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('smoothie') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF47') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF48') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF49') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('watermelon') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF4A') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('Tangerine') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF4C') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF4E') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF50') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('peach') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF51') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDF45') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('Tomato') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

print 'complete!'
