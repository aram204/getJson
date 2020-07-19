from urllib.request import urlopen
import json
with urlopen("https://swapi.dev/api/people/1/") as f:
    source = f.read()
data = json.loads(source)
code = json.dumps(data, indent = 2)
with open("file.json","w") as f:
    f.write(html)
