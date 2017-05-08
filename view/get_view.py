from pip._vendor import requests
import json

r = requests.get("http://localhost:15984/cloud2/_design/transport/_view/tram")
print r.content
