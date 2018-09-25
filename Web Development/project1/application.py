import os
from hashlib import sha1 as hash

from flask import Flask, session, render_template, request, url_for, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from goodreadsapi import get_book_data

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')

    check = db.execute("""SELECT id FROM Users WHERE login=:username""", request.form)
    if check.fetchone():
        return render_template('register.html', error_message="User name already taken")

    data = {
        "pass": hash(request.form['password'].encode()).hexdigest(),
        "login": request.form['username']
        }
    db.execute("""INSERT INTO Users (login, name, email, age, gender)
                  VALUES (:username, :name, :email, :age, :gender)""", request.form)
    db.execute("""UPDATE Users SET password=:pass WHERE login=:login""", data)
    db.commit()
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    password, id, name = db.execute("""SELECT password, id, name FROM Users WHERE login=:username""", request.form).fetchone()
    if password == hash(request.form['password'].encode()).hexdigest():
        session['user_data'] = {
            "id": id,
            "name": name
        }
        return render_template('login.html', error_message="You are logged in!")

    return render_template('index.html')

@app.route('/logout')
def logout():
    session['user_data'] = None
    return render_template('general.html', message="You are now logged out!")

@app.route('/search', methods=["GET"])
def search():
    if not session["user_data"]:
        return render_template('general.html', message="You have to be logged in to search!")
    payload = {
        "title": "%{}%".format(request.args.get("title")),
        "author": "%{}%".format(request.args.get("author")),
        "isbn": "%{}%".format(request.args.get("isbn"))
        }

    result = db.execute("""SELECT Books.title, Books.id FROM Books JOIN Authors
                           ON Books.author_id=Authors.id
                           WHERE Books.title LIKE :title
                           AND Authors.name LIKE :author
                           AND Books.isbn LIKE :isbn""",
                        payload).fetchall()
    if not result:
        return render_template('general.html', message="I found nothing!")
    return render_template('search.html', result=result)

@app.route('/books/<id>')
def books(id):
    result = db.execute("""SELECT Authors.name, Books.title, Books.isbn, Books.year, Books.id
                           FROM Books Join Authors ON Books.author_id=Authors.id
                           WHERE Books.id=:id""",
                        {"id": id}).fetchone()
    reviews = db.execute("""SELECT Reviews.review, Reviews.rating, Users.name
                            FROM Reviews JOIN Users
                            ON Reviews.user_id=Users.id
                            WHERE book_id=:book_id""",
                         {"book_id": id}).fetchall()
    reviewed = True if db.execute("""SELECT * FROM Reviews
                                      WHERE user_id=:user_id AND book_id=:book_id""",
                                   {"user_id": session["user_data"]["id"],
                                    "book_id": id}).fetchone() else False
    goodreads = get_book_data(result[2])
    return render_template("books.html",
                           r=result,
                           reviews=reviews,
                           reviewed=reviewed,
                           goodreads=goodreads)

@app.route('/submit_review', methods=["POST"])
def submit_review():
    db.execute("""INSERT INTO Reviews (book_id, user_id, review, rating)
                  VALUES (:book_id, :user_id, :review, :rating)""",
               {"book_id": request.form["book"],
                "user_id": session["user_data"]["id"],
                "review": request.form["rev"],
                "rating": request.form["rating"]})
    db.commit()
    return redirect(url_for('books', id=request.form["book"]))
