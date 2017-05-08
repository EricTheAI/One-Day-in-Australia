import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@130.56.248.231:5984/')
print couch
db = couch[sys.argv[1]]
print db
view = ViewDefinition('category', 'food', 
'''
function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || doc.metadata.place.name == 'Sydney')

regex=/(#| |^)(kfc|maccas|mcdonald|hungry jack|hungryjack|fries|subway|chips|burger|combo|nugget|big mac|whopper|coke|hot dog|hotdog)( |$|s|es)|\uD83C\uDF54|\uD83C\uDF5F|\uD83C\uDF55|\uD83C\uDF2D/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'junkfood',doc._id,doc.metadata.coordinates.coordinates,doc.metadata.created_at], 1); 

regex=/(#| |^)(whole-grain|whole grain|wholegrain|fruit|melon|orange|apple|pear|grapes|banana|berries|protein powder|proteinpowder|olive oil|oliveoil|celery|celeries|avocado|whole wheat|whole-wheat|wholegrain|almond|smoothie|watermelon|yangerine|peach|tomato)( |$|s|es)|\uD83C\uDF47|\uD83C\uDF49|\uD83C\uDF4A|\uD83C\uDF4C|\uD83C\uDF4E|\uD83C\uDF50|\uD83C\uDF51|\uD83C\uDF45/i
constraint_2 = doc.metadata.text.match(regex)
if(constraint_1 && constraint_2) 
emit([doc.metadata.place.name,'healthyfood',doc._id,doc.metadata.coordinates.coordinates,doc.metadata.created_at], 1); 
}''',
'''function (keys, values, rereduce) {if (rereduce) {return sum(values);} else {return values.length;}}''')
view.sync(db)

print 'complete!'
