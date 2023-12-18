
# Sania Khaja
# CS 341 Spring 2023
# Project #2
# Python, SQL
# data tier, object tier and presentation tier program
# This implements the presentation tier portion

import sqlite3
import objecttier


###########################################
# general stats
# prints out the total number of movies and reviws in the database
###########################################
def general_stats(dbConn):
  print("General stats:")
  print("  # of movies:", f"{objecttier.num_movies(dbConn):,}")
  print("  # of reviews:", f"{objecttier.num_reviews(dbConn):,}")


###########################################
# getMovies
# gets movies related to user input from objectier get_movies functions
# if over a 100 movies queried, does not ouput movies
# outputs movies id, title, year of release
###########################################
def getMovies(dbConn):
  userMovie = input("Enter movie name (wildcards _ and % supported): ")
  movies = objecttier.get_movies(dbConn, userMovie)
  print()
  print("# of movies found:", len(movies))
  # checking if too many movies queried and if so prints message
  if (len(movies) > 100):
    print(
      "There are too many movies to display, please narrow your search and try again..."
    )
  else:
    # prints all movies with id, title and release year
    for movie in movies:
      print(movie.Movie_ID, ":", movie.Title, f"({movie.Release_Year:})")


###########################################
# getMovieDetails
# user inputs a movie id and gets all movie details
# Movie_ID, Title, Release_Date, Runtime, Original_Language, Budget, Revenue, Num_Reviews, Avg_Rating, Tagline, Genres: list of string, Production_Companies: list of string
###########################################
def getMovieDetails(dbConn):
  userMovieID = input("Enter movie id: ")
  print()
  movie = objecttier.get_movie_details(dbConn, userMovieID)
  # printing movie details an if none then says so
  if (movie == None):
    print("No such movie...")
    print()
  else:
    print(movie.Movie_ID, ":", movie.Title)
    print("  Release date:", f"{movie.Release_Date:}")
    print("  Runtime:", movie.Runtime, "(mins)")
    print("  Orig language:", movie.Original_Language)
    print("  Budget:", f"${movie.Budget:,}", "(USD)")
    print("  Revenue:", f"${movie.Revenue:,}", "(USD)")
    print("  Num reviews:", movie.Num_Reviews)
    print("  Avg rating:", f"{movie.Avg_Rating:.2f}", "(0..10)")
    print("  Genres:", end=" ")
    for genre in movie.Genres:
      print(genre, end=", ")
    print()
    print("  Production companies:", end=" ")
    for prod in movie.Production_Companies:
      print(prod, end=", ")
    print()
    print("  Tagline:", movie.Tagline)
    print()


###########################################
# getTopNMovies
# Gets user input for top N movies and min number of reviews
# displays id, title, year, avg rating, and review amount based on user input
# # makes sure review amount is positive and top N is positive
###########################################
def getTopNMovies(dbConn):
  userTopN = input("N? ")
  # checking for valid number of top N
  if (int(userTopN) < 0):
    print("Please enter a positive value for N...")
    print()
  else:
    userMinRev = input("min number of reviews? ")
    # checking for valid amount of reviews
    if (int(userMinRev) <= 0):
      print("Please enter a positive value for min number of reviews...")
      print()
    else:
      print()
      topNMovies = objecttier.get_top_N_movies(dbConn, int(userTopN),
                                               int(userMinRev))
      # printing id, title, year, rating and num reviews for every movie in top N
      for movie in topNMovies:
        print(movie.Movie_ID, ":", movie.Title, f"({movie.Release_Year:}),",
              "avg rating =", f"{movie.Avg_Rating:.2f}",
              f"({movie.Num_Reviews:} reviews)")
      print()


###########################################
# insertReview
# inserts new review into table based on user input rating and movie_id
# makes sure review num is between 0 and 10 and top N is positive
# if able to add review into database, then says that the review was successflly inserted
###########################################
def insertReview(dbConn):
  inputRating = input("Enter rating (0..10): ")
  if (int(inputRating) > 10 or int(inputRating) < 0):
    print("Invalid rating...")
    print()
  else:
    inputMovieID = input("Enter movie id: ")
    print()
    movie = objecttier.add_review(dbConn, int(inputMovieID), int(inputRating))
    # if movie_id does not exist
    if (movie == 0):
      print("No such movie...")
      print()
    else:  # movie id exists so database review could be added
      print("Review successfully inserted")
      print()


###########################################
# setTagline
# sets tagline for a given movie by getting tagline and movie_id from user
# if movie_id does not exist, tells user. Otherwise says that tagline was successfully set
###########################################
def setTagline(dbConn):
  inputTag = input("tagline? ")
  inputMovieID = input("movie id? ")
  print()
  movie = objecttier.set_tagline(dbConn, int(inputMovieID), inputTag)
  # if movie_id does not exist
  if (movie == 0):
    print("No such movie...")
    print()
  else:  # movie id exists so database review could be added
    print("Tagline successfully set")
    print()


###########################################
# main
###########################################
print("** Welcome to the MovieLens app **")
dbConn = sqlite3.connect('MovieLens.db')

print()
general_stats(dbConn)
print()

userInput = input("Please enter a command (1-5, x to exit): ")

while userInput != "x":
  print()
  if userInput == "1":
    getMovies(dbConn)
  elif (userInput == "2"):
    getMovieDetails(dbConn)
  elif (userInput == "3"):
    getTopNMovies(dbConn)
  elif (userInput == "4"):
    insertReview(dbConn)
  elif (userInput == "5"):
    setTagline(dbConn)

  userInput = input("Please enter a command (1-5, x to exit): ")
