import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

original_badges_json = "https://api.kongregate.com/badges.json" # api.kongregate.com and www.kongregate.com both work
badges_json = "./kongregate/badges.json"
badges_file = "./kongregate/badges.js"
achievements_page = "https://www.kongregate.com/en/achievements?sort=newest"

with open(badges_file, "r", encoding="utf-8") as f:
    exec(str(f.read())) # Reminder: badges.js assigns the content of badges.json to a variable named badges

badges_dict = {}
for b in badges:
    badges_dict[b["id"]] = b

try:
    new_badges = json.load(urlopen(original_badges_json))
except:
    # If badges.json is unavailable, then most recent new badges will be created manually based on the achievements page
    new_badges = []
    page = BeautifulSoup(urlopen(achievements_page), features="html.parser")
    achievements = page.body.find(id="achievements").find_all("a")
    for achievement in achievements:
        badge_url = achievement.img["src"]
        ps=achievement.find_all("p")
        bdg = {}
        bdg["id"] = ( int(re.search("[0-9]{4}\/[0-9]{4}",badge_url).group().replace("/","")) + 1 ) // 2
        bdg["name"] = achievement.img["alt"]
        bdg["created_at"] = "unknown" # Cannot be retrieved from the achievements page
        bdg["icon_url"] = achievement.img["src"]
        bdg["games"] = [{"title": ps[0].get_text(strip=True), "url": achievement["href"][0:achievement["href"].find("?")]}]
        bdg["points"] = int(achievement.span.get_text(strip=True)[0:achievement.span.get_text(strip=True).find(" ")])
        bdg["difficulty"] = {5:"easy", 15:"medium", 30:"hard", 60:"impossible"}[bdg["points"]]
        bdg["description"] = ps[1].get_text(strip=True)
        bdg["users_count"] = 0 # Cannot be retrieved from the achievements page
        if bdg["id"] in badges_dict:
            # Let us avoid to overwrite previously valid data simply because we could not find it.
            # However, we still keep this badge here, in case other values changed.
            bdg["created_at"] = badges_dict[bdg["id"]]["created_at"]
            bdg["users_count"] = badges_dict[bdg["id"]]["users_count"]
        new_badges.append(bdg)
finally:
    changes_counter = 0
    for b in new_badges:
        if b not in badges: # If badge did not exist OR if something changed about this badge
            badges_dict[b["id"]] = b
            changes_counter += 1
    updated_badges = [y for x,y in sorted(badges_dict.items())]
    if changes_counter:
        with open(badges_json, 'w+', encoding="utf-8") as f:
            json.dump(updated_badges, f)
        with open(badges_file,"w",encoding="utf-8") as f:
            f.write("badges="+str(updated_badges)+";")