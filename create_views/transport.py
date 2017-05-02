#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import couchdb
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch['cloud2']

#1.tram
view = ViewDefinition('transport', 'tram', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('tram') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE8B') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE8A') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#2.rail
view = ViewDefinition('transport', 'rail', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('train') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('rail') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('metro') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE86') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE89') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE87') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#3.taxi
view = ViewDefinition('transport', 'taxi', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('taxi') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE95') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE96')
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#4.bus
view = ViewDefinition('transport', 'bus', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('bus') != -1||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE8C') != -1||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE8D') != -1||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE8F') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#5.walk
view = ViewDefinition('transport', 'walk', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('walk') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('walking') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEB6') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#6.bike
view = ViewDefinition('transport', 'bike', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('bike') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('bicycle')!= -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEB4')!= -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEB5\u200D')!= -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#7.car
view = ViewDefinition('transport', 'car', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('drive') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('driving') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE97')!= -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE98')!= -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#8.airplane
view = ViewDefinition('transport', 'airplane', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('airplane') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\u2708') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEE9')!= -1  ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEEB')!= -1  ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEEC')!= -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)


#8.airplane
view = ViewDefinition('transport', 'ferry', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('ferry') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\u26F4') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#9.light rail
view = ViewDefinition('transport', 'light_rail', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('light rail') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDE88') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#10.uber
view = ViewDefinition('transport', 'uber', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('uber') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.text], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)


print 'complete!'
