import re,json
from pip._vendor import requests
import ast
from demjson import encode

with open("rest.json","r") as f:
    for line in f:
        id = str(re.findall("(?<='id': )[\d]+",line)[0])
        json = ast.literal_eval(line)
        tweet = encode(json)
        r=requests.put("http://localhost:5984/rest/"+id,data='{"category":"melbourne","metadata":'+tweet+'}')
        if r.status_code!=409 and r.status_code!=201:
            print r.status_code,r.content,id
            print tweet

with open("finish_rest.txt","w") as fp:
    fp.write("finish rest.json")
    fp.close()
