import os
from json import loads
from urllib.parse import urlencode
from urllib.request import urlopen

def get_book_data(isbn):
    api_key = os.getenv("G_KEY")
    url = "https://www.goodreads.com/book/review_counts.json"
    parameters = {"key": api_key,
                  "isbns": isbn,
                  "format": "json"
                  }
    try:
        resp = urlopen(url + "?" + urlencode(parameters))
        resp = loads(resp.read().decode())
        book_data = resp["books"][0]
        ratings_count = book_data["ratings_count"]
        average_rating = book_data["average_rating"]
    except Exception as e:
        if e.code == 404:
            n_of_ratings = None
            ave_rating = None

    return {"ratings_count": ratings_count, "average_rating": average_rating}  
