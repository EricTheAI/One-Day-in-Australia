# -*- coding: utf-8 -*-
from pip._vendor import requests
import json

# save json
with open('tinyTwitter.json', "r") as fp:
    fp.readline()
    while not fp.readline()==None:
        line = fp.readline()
        j=json.loads(line[0:-2])
        id=j["meta"]["id"]
        r=requests.put("http://130.56.248.231:5985/cloud/"+id,data='{"category":"tinyTwitter","metadata":'+line[0:-2]+'}')
        print r.status_code
        print r.content

# get view
# tweeter catagory and tweeter text
r = requests.get("http://130.56.248.231:5985/cloud/_design/view1/_view/view1")
print r.content