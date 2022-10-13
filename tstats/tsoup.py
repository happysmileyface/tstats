import json
#sx = s.get("https://ch.tetr.io/api/users/whatspoppin").json()
with open("user.json", "r+") as file:
    x=json.load(file)
    #json.dump(sx, file)
    #{"success": true, "data": {"user": {"_id": "5f8145491404653c00f8df0a", "username": "whatspoppin", "role": "user", "ts": "2020-10-10T05:23:21.711Z", "badges": [{"id": "secretgrade", "label": "Achieved the full Secret Grade", "ts": "2022-04-28T00:46:28.283Z"}], "xp": 668500, "gamesplayed": 465, "gameswon": 120, "gametime": 295536.22733333375, "country": "US", "supporter_tier": 0, "verified": false, "league": {"gamesplayed": 133, "gameswon": 73, "rating": 19907.077389661612, "glicko": 1857.0415561231769, "rd": 62.39379724864633, "rank": "s", "apm": 46.8, "pps": 1.9, "vs": 93.31, "decaying": false, "standing": 6734, "percentile": 0.17138420811485008, "standing_local": 1374, "prev_rank": "s-", "prev_at": 9035, "next_rank": "s+", "next_at": 6679, "percentile_rank": "s"}, "avatar_revision": 1619155110064, "friend_count": 1}}, "cache": {"status": "miss", "cached_at": 1665637223602, "cached_until": 1665637523602}}
data=x["data"]
user=data["user"]
league=user["league"]
#print(league["rank"])
#should print "s"
#dumps json dict to user.json