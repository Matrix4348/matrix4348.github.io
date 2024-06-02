import json
from urllib.request import urlopen

badges_file="./kongregate/badges.js"

badges=json.load(urlopen("https://www.kongregate.com/badges.json"))
with open(badges_file,"w",encoding="utf-8") as f:
    f.write("badges="+str(badges)+";")