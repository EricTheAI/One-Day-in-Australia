import string,re,json,ast
import os.path
from pip._vendor import requests
from demjson import encode
from pathlib2 import Path

f1 = open("fail_twitter.json",'w')
for i in ['a','b','c']:
	for j in string.ascii_lowercase:
		fname = "mel_"+i+j
		print fname
		if Path(fname).is_file():
			with open(fname) as f:
				for line in f:
					try:
						id = str(re.findall("(?<='id': )[\d]+",line)[0])
						json = ast.literal_eval(line)
						tweet = encode(json)
						r=requests.put("http://localhost:5984/rest/"+id,data='{"category":"melbourne","metadata":'+tweet+'}')
						if r.status_code!=409:
							print r.status_code,r.content
					except:
						f1.write(line)
			os.remove(fname)
f1.close()
