#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch[sys.argv[1]]

#1.ski
view = ViewDefinition('sport', 'ski', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('ski') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\u26F7') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('snowboard') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFC2') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFBF') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','ski'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#2.golf
view = ViewDefinition('sport', 'golf', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('golf') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFCC') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\u26F3') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('flag in hole') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','golf'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#3.surf
view = ViewDefinition('sport', 'surf', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('surf') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFC4') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','surf'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#4.swim
view = ViewDefinition('sport', 'swim', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('swim') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFCA') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','swim'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#5.bike
view = ViewDefinition('sport', 'bike', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('biking') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEB4') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83D\uDEB5') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','bike'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#6.soccer
view = ViewDefinition('sport', 'soccer', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('soccer') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\u26BD') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','soccer'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#7.baseball
view = ViewDefinition('sport', 'baseball', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('baseball') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\u26BE') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','baseball'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#8.basketball
view = ViewDefinition('sport', 'basketball', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('basketball') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFC0') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','basketball'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#9.volleyball
view = ViewDefinition('sport', 'volleyball', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('volleyball') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFD0') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','volleyball'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#10.football
view = ViewDefinition('sport', 'football', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('football') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFC8') != -1 || 
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFC9') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','football'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#11.tennis
view = ViewDefinition('sport', 'tennis', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('tennis') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFBE') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','tennis'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#12.bowling
view = ViewDefinition('sport', 'bowling', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('bowling') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('strike') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFB3') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','bowling'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#13.pingpong
view = ViewDefinition('sport', 'pingpong', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('pingpong') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFD3') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','pingpong'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#14.badminton
view = ViewDefinition('sport', 'badminton', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('badminton') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFF8') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','badminton'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#15.boxing
view = ViewDefinition('sport', 'boxing', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('boxing') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83E\uDD4A') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','boxing'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#16.skate
view = ViewDefinition('sport', 'skate', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('skate') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('skating') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\u26F8') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','skate'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#17.jogging
view = ViewDefinition('sport', 'jogging', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('jogging') != -1 ||
doc.metadata.json.text.toLowerCase().indexOf('\uD83C\uDFC3') != -1 
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','jogging'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

#18.gym
view = ViewDefinition('sport', 'gym', 
'''function(doc) {
constraint_1 = (doc.metadata.json.place.name == 'Melbourne' || 
doc.metadata.json.place.name == 'Sydney')
constraint_2 = doc.metadata.json.text.toLowerCase().indexOf('gym') != -1
if(constraint_1 && constraint_2) 
emit([doc.metadata.json.place.name,doc.metadata.json.coordinates.coordinates,doc.metadata.json.created_at,'sport','gym'], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)



print 'complete!'

