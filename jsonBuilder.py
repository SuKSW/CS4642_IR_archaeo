import json
import time

f=open("../data/archeo.jl", "r")
jsonl_content = ""
if f.mode == 'r':
    jsonl_content = f.read()

time.sleep(.300)
result = []
for jline in jsonl_content.split('\n'):
    if jline != "":
        result.append(json.loads(jline))
print jsonl_content

f1 = open("../data/archeo.json", "w+")
f1.write(json.dumps(result))
f1.close()
