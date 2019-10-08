import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# checks that database exists or is accessible
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# connects to database and creates db
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# opens books file
with open("books.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # inserts title, isbn, author, and year published into the books database
    for row in csv_reader:
        if row[0] != "isbn":
            db.execute("INSERT INTO books (title, isbn, author, yearPublished) VALUES (:title, :isbn, :author, :yearPublished)",
                        {"title": row[1], "isbn": row[0], "author": row[2], "yearPublished":row[3]})
    db.commit()
