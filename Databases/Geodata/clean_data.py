import sqlite3, json

conn = sqlite3.connect("raw_data.sqlite")
cur = conn.cursor()

output = []

places = cur.execute("SELECT data FROM Places")
for place in places:
    lat = json.loads(place[0])["result"]["geometry"]["location"]["lat"]
    lng = json.loads(place[0])["result"]["geometry"]["location"]["lng"]
    name = json.loads(place[0])["result"]["name"]

    output.append({"lat": lat,
                   "lng": lng,
                   "name": name})

with open("locations.json", "w") as f:
    s = json.dumps(output)
    f.write("var locations = " + s)
