# File: objecttier.py
#
# objecttier
#
# Builds Movie-related objects from data retrieved through
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#
import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:

  def __init__(self, id, title, releaseYr):
    self._Movie_ID = id
    self._Title = title
    self._Release_Year = releaseYr

  @property
  def Movie_ID(self):
    return self._Movie_ID

  @property
  def Title(self):
    return self._Title

  @property
  def Release_Year(self):
    return self._Release_Year


##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:

  def __init__(self, id, title, releaseYr, numReviews, avgRatings):
    self._Movie_ID = id
    self._Title = title
    self._Release_Year = releaseYr
    self._Num_Reviews = numReviews
    self._Avg_Rating = avgRatings

  @property
  def Movie_ID(self):
    return self._Movie_ID

  @property
  def Title(self):
    return self._Title

  @property
  def Release_Year(self):
    return self._Release_Year

  @property
  def Num_Reviews(self):
    return self._Num_Reviews

  @property
  def Avg_Rating(self):
    return self._Avg_Rating


##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:

  def __init__(self, id, title, releaseDate, runtime, originalLang, budget,
               revenue, numReviews, avgRating, tagline, genres,
               productionComp):
    self._Movie_ID = id
    self._Title = title
    self._Release_Date = releaseDate
    self._Runtime = runtime
    self._Original_Language = originalLang
    self._Budget = budget
    self._Revenue = revenue
    self._Num_Reviews = numReviews
    self._Avg_Rating = avgRating
    self._Tagline = tagline
    self._Genres = genres
    self._Production_Companies = productionComp

  @property
  def Movie_ID(self):
    return self._Movie_ID

  @property
  def Title(self):
    return self._Title

  @property
  def Release_Date(self):
    return self._Release_Date

  @property
  def Runtime(self):
    return self._Runtime

  @property
  def Original_Language(self):
    return self._Original_Language

  @property
  def Budget(self):
    return self._Budget

  @property
  def Revenue(self):
    return self._Revenue

  @property
  def Num_Reviews(self):
    return self._Num_Reviews

  @property
  def Avg_Rating(self):
    return self._Avg_Rating

  @property
  def Tagline(self):
    return self._Tagline

  @property
  def Genres(self):
    return self._Genres

  @property
  def Production_Companies(self):
    return self._Production_Companies


##################################################################
#
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
  sql = "SELECT COUNT(Movie_ID) FROM Movies"
  totalMovieRows = datatier.select_one_row(dbConn, sql)
  if (totalMovieRows == None):
    return -1
  else:
    return totalMovieRows[0]


##################################################################
#
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
  sql = "SELECT COUNT(Rating) FROM Ratings"
  totalReviewRows = datatier.select_one_row(dbConn, sql)
  if (totalReviewRows == None):
    return -1
  else:
    return totalReviewRows[0]


##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by name;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
  sql = "SELECT Movie_ID, Title, strftime('%Y', Release_Date) FROM Movies WHERE Title LIKE ? ORDER BY Movie_ID ASC"
  movieRows = datatier.select_n_rows(dbConn, sql, [pattern])
  list = []
  if (movieRows != None or len(movieRows) != 0):
    for row in movieRows:
      objectMovie = Movie(row[0], row[1], row[2])
      list.append(objectMovie)

  return list


##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):
  sql = "SELECT Movies.Movie_ID, Movies.Title, DATE(Movies.Release_Date), Movies.Runtime, Movies.Original_Language, Movies.Budget, Movies.Revenue, COUNT(Ratings.Rating), AVG(Ratings.Rating), Movie_Taglines.Tagline, GROUP_CONCAT(DISTINCT(Genres.Genre_Name)), GROUP_CONCAT(DISTINCT(Companies.Company_Name)) FROM Movies LEFT JOIN Ratings ON Movies.Movie_ID = Ratings.Movie_ID LEFT JOIN Movie_Taglines ON Movies.Movie_ID = Movie_Taglines.Movie_ID LEFT JOIN Movie_Genres ON Movies.Movie_ID = Movie_Genres.Movie_ID LEFT JOIN Genres ON Movie_Genres.Genre_ID = Genres.Genre_ID LEFT JOIN Movie_Production_Companies ON Movies.Movie_ID = Movie_Production_Companies.Movie_ID LEFT JOIN Companies ON Movie_Production_Companies.Company_ID = Companies.Company_ID WHERE Movies.Movie_ID = ?"

  # query to get number of reviews
  sqlNumRev = "SELECT COUNT(Ratings.Rating) FROM Movies LEFT JOIN Ratings ON Movies.Movie_ID = Ratings.Movie_ID WHERE Movies.Movie_ID = ? "
  # queries rows
  movieRow = datatier.select_one_row(dbConn, sql, [movie_id])
  movieNumRev = datatier.select_one_row(dbConn, sqlNumRev, [movie_id])

  # checking for no movie id match
  if (movieRow[0] == None or len(movieRow) == 0):
    return None

  # starter values for scenarios where there are multiple items or possible blanks
  listGenres = []
  tempGenre = ""
  listCompanies = []
  tempCompany = ""
  tagline = ""
  avgRating = 0.00
  numRating = 0
  revenue = 0
  budget = 0

  # if query item not blank, setting to query result
  if (movieRow[5] != None):
    budget = movieRow[5]

  if (movieRow[6] != None):
    revenue = movieRow[6]

  if (movieRow[7] != None):
    numRating = movieNumRev[0]

  if (movieRow[8] != None):
    avgRating = movieRow[8]

  if (movieRow[9] != None):
    tagline = movieRow[9]

  # storing multiple genres in a list if genres exist
  if (movieRow[10] != None):
    for genre in movieRow[10]:
      if (genre == ","):
        listGenres.append(tempGenre)
        tempGenre = ""
      else:
        tempGenre += genre
    listGenres.append(tempGenre)

  # storing multiple companies in a list if not blank
  if (movieRow[11] != None):
    for company in movieRow[11]:
      if (company == ","):
        listCompanies.append(tempCompany)
        tempCompany = ""
      else:
        tempCompany += company
    listCompanies.append(tempCompany)

  # sorting lists by alphabetical order
  listGenres.sort()
  listCompanies.sort()

  # creating object
  objectMovie = MovieDetails(
    movieRow[0],
    movieRow[1],
    movieRow[2],
    movieRow[3],
    movieRow[4],
    budget,
    revenue,
    numRating,
    avgRating,
    tagline,
    listGenres,
    listCompanies,
  )
  return objectMovie


##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
  sql = "SELECT Ratings.Movie_ID, Movies.Title, strftime('%Y', Release_Date), COUNT(Ratings.Rating), AVG(Ratings.Rating) FROM Movies JOIN Ratings ON Movies.Movie_ID = Ratings.Movie_ID GROUP BY Ratings.Movie_ID HAVING COUNT(Rating) >= ? ORDER BY AVG(Ratings.Rating) DESC LIMIT ?"

  movieRows = datatier.select_n_rows(dbConn, sql, [min_num_reviews, N])
  list = []
  for row in movieRows:
    objectMovie = MovieRating(row[0], row[1], row[2], row[3], row[4])
    list.append(objectMovie)

  return list


##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
  movieExists = "SELECT COUNT(Movies.Movie_ID) FROM Movies WHERE Movie_ID = ?"
  movieRows = datatier.select_one_row(dbConn, movieExists, [movie_id])
  # if no movie id exists then returns 0, else inserts value into table
  if (movieRows[0] == 0):
    return 0
  else:
    sql = "INSERT INTO Ratings (Movie_ID, Rating) VALUES (?, ?)"
    modified = datatier.perform_action(dbConn, sql, [movie_id, rating])
    if (modified == -1):
      return 0
    return 1


##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
  movieExists = "SELECT COUNT(Movie_ID) FROM Movies WHERE Movie_ID = ?"
  movieRows = datatier.select_one_row(dbConn, movieExists, [movie_id])
  # checking if movie_id exists in database
  if (movieRows[0] == 0):
    return 0
  else:
    movieExistsTag = "SELECT COUNT(Movie_ID) FROM Movie_Taglines WHERE Movie_ID = ?"
    movieRowsTag = datatier.select_one_row(dbConn, movieExistsTag, [movie_id])
    # checking if movie_id exists in table and if not then inserts tagline and id into table
    if (movieRowsTag[0] == 0):
      sql = "INSERT INTO Movie_Taglines (Movie_ID, Tagline) VALUES (?, ?)"
      modified = datatier.perform_action(dbConn, sql, [movie_id, tagline])
      if (modified == -1):
        return 0
    else:  # updates movie_id tagline if already exists
      sql = "UPDATE Movie_Taglines SET Tagline = ? WHERE Movie_ID = ?"
      modified = datatier.perform_action(dbConn, sql, [tagline, movie_id])
    return 1
