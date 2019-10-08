CREATE TABLE users (
  id  SERIAL PRIMARY KEY,
  dateJoined DATE,
  posts INTEGER DEFAULT 0,
  username VARCHAR NOT NULL,
  passwd VARCHAR NOT NULL
);


CREATE TABLE reviews (
  isbn VARCHAR NOT NULL,
  title VARCHAR NOT NULL,
  review VARCHAR NOT NULL,
  username VARCHAR NOT NULL,
  rating INT NOT NULL
);


CREATE TABLE books (
  title VARCHAR,
  isbn VARCHAR,
  author VARCHAR,
  yearPublished VARCHAR
);
