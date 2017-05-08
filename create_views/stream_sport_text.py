#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@localhost:15984/')
print couch
db = couch[sys.argv[1]]
print db
view = ViewDefinition('category', 'sport_text', 
'''
function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
doc.metadata.place.name == 'Sydney')

var date = new Date(doc.metadata.created_at).toString();

regex=/(#| |^)(ski|snowboard|skiing|skiied)( |$|s|es|ed)|\u26F7|\uD83C\uDFC2|\uD83C\uDFBF/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'ski',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(golf|flag in hole)( |ing|$|s|es|ed)|\uD83C\uDFCC|\u26F3/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'golf',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(surf)( |ing|$|s|es|ed)|\uD83C\uDFC4/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'surf',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(swim|swimming)( |$|s|es|ed)|\uD83C\uDFCA/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'swim',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(biking|bike|bicycle|bicycling)( |$|s|es|ed|d)|\uD83D\uDEB4|\uD83D\uDEB5/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'bike',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(soccer)( |$|s|es|ed)|\u26BD/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'soccer',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(baseball)( |$|s|es|ed)|\u26BE/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'baseball',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(basketball)( |$|s|es|ed)|\uD83C\uDFC0/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'basketball',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(volleyball)( |$|s|es|ed)|\uD83C\uDFD0/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'volleyball',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(football)( |$|s|es|ed)|\uD83C\uDFC8|\uD83C\uDFC9/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'football',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(tennis)( |$|s|es|ed)|\uD83C\uDFBE/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'tennis',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(bowling)( |$|s|es|ed)|\uD83C\uDFB3/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'bowling',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(pingpong|table tennis)( |$|s|es|ed)|\uD83C\uDFD3/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'pingpong',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(badminton)( |$|s|es|ed)|\uD83C\uDFF8/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'badminton',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(boxing)( |$|s|es|ed)|\uD83E\uDD4A/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'boxing',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(skate|skating)( |$|s|es|ed|d)|\u26F8/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'skate',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(jogging|running|run)( |$|s|es|ed)|\uD83C\uDFC3/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'run',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);

regex=/(#| |^)(gym)/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'gym',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);
}
''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

print 'complete!'

