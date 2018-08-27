import sqlite3, json, sys
import urllib.parse, urllib.request

conn = sqlite3.connect("raw_data.sqlite")
cur = conn.cursor()

with open("secret.json") as f:
    api_key = json.load(f)["api_key"]

def get_single(name):
    cur.execute("SELECT id from Places WHERE name = ?", (name, ))
    if cur.fetchone():
        print("{} already in database!".format(name))
        return None
    # Get place id
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    params = {"key": api_key,
              "input": name,
              "inputtype": "textquery"}

    get_url = url + urllib.parse.urlencode(params)
    with urllib.request.urlopen(get_url) as f:
        try:
            place_id = json.load(f)["candidates"][0]["place_id"]
        except:
            print("Couldn't add {} to database!".format(name))
            return None

    # Get details of given place
    url = "https://maps.googleapis.com/maps/api/place/details/json?"
    params = {"key": api_key,
              "placeid": place_id}

    get_url = url + urllib.parse.urlencode(params)
    with urllib.request.urlopen(get_url) as f:
        data = f.read().decode()

    cur.execute("INSERT INTO Places (name, data) VALUES (?,?)", (name, data))
    conn.commit()
    print("Added {} to database!".format(name))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for place in f:
            get_single(place[:-1])
