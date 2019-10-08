# Project 1

Web Programming with Python and JavaScript

CS50 Books -

The static folder has a number of images that I use in the webpage and the style sheets.

The templates folder:
  about.html - the about page containing virtually nothing
  api.html - the layout for anytime someone makes a call to the api for a specific book
  books.html - the dynamic webpage for any of the 5000 books in the books database
  error.html - a simple dynamic page that allows an error message to be fed in
  index.html - the home page, has links to pretty much everything else on the site and allows users to register and login (or logout)
  layout.html - the layout for all of the other pages (except error.html)
  login.html - the login page, you are redirected here after registering
  profile.html - says "welcome (name of user)", shows the reviews the user has made
  register.html - has three inputs - username, password, and password confirmation
  search.html - the search page, the search button is pretty cool

The Databases:
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
