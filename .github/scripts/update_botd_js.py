from urllib.request import urlopen

botd_file="./kongregate/botd.js"

page=str(urlopen("https://www.kongregate.com").read())
l=len("botd_badge_id")
x=page.find("botd_badge_id")
i1=page.find(":",x)+1
i2=min(page.find(",",x),page.find("{",x))
botd_badge_id=page[i1:i2]

with open(botd_file,"w") as f:
    f.write("botd="+botd_badge_id+";")