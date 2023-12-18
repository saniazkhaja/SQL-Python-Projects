
#
# header comment! Overview, name, etc.
# Name: Sania Khaja
# Class: CS 341
# Languages utilized: Python and SQL
# This program allows a user to choose between 9 different options which gets different
# information from the CTA database. Some of these options allow for further user input
# Options 6 to 9 allow for plotting data

import sqlite3
import matplotlib.pyplot as plt


##################################################################
#
# print_stats
#
# Given a connection to the CTA database, executes various
# SQL queries to retrieve and output basic stats.
#
def print_stats(dbConn):
  dbCursor = dbConn.cursor()

  print("General stats:")

  # number of stations
  dbCursor.execute("SELECT COUNT(*) FROM Stations;")
  rowCountStations = dbCursor.fetchone()
  print("  # of stations:", f"{rowCountStations[0]:,}")

  # number of stops
  dbCursor.execute("SELECT COUNT(*) FROM Stops;")
  rowCountStops = dbCursor.fetchone()
  print("  # of stops:", f"{rowCountStops[0]:,}")

  # number of ride entries
  dbCursor.execute("SELECT COUNT(*) FROM Ridership;")
  rowRide = dbCursor.fetchone()
  print("  # of ride entries:", f"{rowRide[0]:,}")

  # date range
  dbCursor.execute("SELECT MIN(DATE(Ride_Date)) FROM Ridership;")
  rowMinDate = dbCursor.fetchone()
  dbCursor.execute("SELECT MAX(DATE(Ride_Date)) FROM Ridership;")
  rowMaxDate = dbCursor.fetchone()
  print("  date range:", f"{rowMinDate[0]:}", "-", f"{rowMaxDate[0]:}")

  # total ridership
  dbCursor.execute("SELECT SUM(Num_Riders) FROM Ridership;")
  totalRiders = dbCursor.fetchone()
  print("  Total ridership:", f"{totalRiders[0]:,}")

  # weekday ridership
  dbCursor.execute(
    "SELECT SUM(Num_Riders) FROM Ridership WHERE Type_of_Day = 'W';")
  rowWeekday = dbCursor.fetchone()
  percentage = (rowWeekday[0] / totalRiders[0]) * 100
  print("  Weekday ridership:", f"{rowWeekday[0]:,}", f"({percentage:.2f}%)")

  # saturday ridership
  dbCursor.execute(
    "SELECT SUM(Num_Riders) FROM Ridership WHERE Type_of_Day = 'A';")
  rowSat = dbCursor.fetchone()
  percentage = (rowSat[0] / totalRiders[0]) * 100
  print("  Saturday ridership:", f"{rowSat[0]:,}", f"({percentage:.2f}%)")

  # sunday/holiday ridership
  dbCursor.execute(
    "SELECT SUM(Num_Riders) FROM Ridership WHERE Type_of_Day = 'U';")
  rowSunHol = dbCursor.fetchone()
  percentage = (rowSunHol[0] / totalRiders[0]) * 100
  print("  Sunday/holiday ridership:", f"{rowSunHol[0]:,}",
        f"({percentage:.2f}%)")


# END OF print_stats


# decides what function to call based on user input
def allCommands(dbConn, userInput):
  if userInput == "1":
    command1(dbConn)

  if userInput == "2":
    command2(dbConn)

  if userInput == "3":
    command3(dbConn)

  if userInput == "4":
    command4(dbConn)

  if userInput == "5":
    command5(dbConn)

  if userInput == "6":
    command6(dbConn)

  if userInput == "7":
    command7(dbConn)

  if userInput == "8":
    command8(dbConn)

  if userInput == "9":
    command9(dbConn)


# END OF allCommands


# executes command1
# retrieves stations that are like users input
def command1(dbConn):
  print()
  dbCursor = dbConn.cursor()
  userInputC1 = input("Enter partial station name (wildcards _ and %): ")
  # querying data
  sqlC1 = "SELECT Station_ID, Station_Name FROM Stations WHERE Station_Name LIKE ? ORDER BY Station_Name ASC;"
  dbCursor.execute(sqlC1, [userInputC1])
  rowStationNames = dbCursor.fetchall()

  if len(rowStationNames) == 0:
    print("**No stations found... ")

  # prints all stations relavent to user input
  for row in rowStationNames:
    if row == "None":
      print("**No stations found... ")
      break
    print(row[0], ":", row[1])
  print()


# END OF command1


# executes command2
# displays all stations with ridership and ridership percent in ascending order
def command2(dbConn):
  dbCursor = dbConn.cursor()

  # querying data
  dbCursor.execute("SELECT SUM(Num_Riders) FROM Ridership;")
  totalRiders = dbCursor.fetchone()
  dbCursor.execute(
    "SELECT Stations.Station_Name, SUM(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID GROUP BY Station_Name;"
  )
  rowAllStations = dbCursor.fetchall()

  print("** ridership all stations **")
  # prints all stations with ridership and percentage
  for row in rowAllStations:
    percentage = (row[1] / totalRiders[0]) * 100
    print(row[0], ":", f"{row[1]:,}", f"({percentage:.2f}%)")
  print()


# END OF command2


# executes command3
# displays top 10 stations with ridership and ridership percent in descending order
def command3(dbConn):
  dbCursor = dbConn.cursor()

  # querying data
  dbCursor.execute("SELECT SUM(Num_Riders) FROM Ridership;")
  totalRiders = dbCursor.fetchone()
  dbCursor.execute(
    "SELECT Stations.Station_Name, SUM(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID GROUP BY Station_Name ORDER BY SUM(Ridership.Num_Riders) DESC LIMIT 10;"
  )
  rowAllStations = dbCursor.fetchall()

  print("** top-10 stations **")
  # prints top 10 stations with ridership and percentage
  for row in rowAllStations:
    percentage = (row[1] / totalRiders[0]) * 100
    print(row[0], ":", f"{row[1]:,}", f"({percentage:.2f}%)")
  print()


# END OF command3


# executes command4
# displays least 10 stations with ridership and ridership percent in ascending order
def command4(dbConn):
  dbCursor = dbConn.cursor()

  # querying data
  dbCursor.execute("SELECT SUM(Num_Riders) FROM Ridership;")
  totalRiders = dbCursor.fetchone()
  dbCursor.execute(
    "SELECT Stations.Station_Name, SUM(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID GROUP BY Station_Name ORDER BY SUM(Ridership.Num_Riders) ASC LIMIT 10;"
  )
  rowAllStations = dbCursor.fetchall()

  print("** least-10 stations **")
  # prints least 10 stations with ridership and percentage
  for row in rowAllStations:
    percentage = (row[1] / totalRiders[0]) * 100
    print(row[0], ":", f"{row[1]:,}", f"({percentage:.2f}%)")
  print()


# END OF command4


# executes command5
# takes in user input line color and outputs all stop names with info direction and ADA that are part of the line
def command5(dbConn):
  print()
  dbCursor = dbConn.cursor()
  userInputColor = input("Enter a line color (e.g. Red or Yellow): ")

  # querying data
  sqlColor = "SELECT Stops.Stop_Name, Stops.Direction, Stops.ADA FROM Stops INNER JOIN StopDetails ON Stops.Stop_ID = StopDetails.Stop_ID INNER JOIN Lines ON StopDetails.Line_ID = Lines.Line_ID WHERE Lines.Color LIKE ? ORDER BY Stop_Name ASC;"
  dbCursor.execute(sqlColor, [userInputColor])
  rowLines = dbCursor.fetchall()

  if len(rowLines) == 0:
    print("**No such line...")

  # prints all rows relavent to user input
  for row in rowLines:
    if row == "None":
      print("**No such line...")
      break
    # using int 0 and 1 to check if accesible or not
    if row[2] == 1:
      print(row[0], ":", "direction =", row[1], "(accessible? yes)")
    else:
      print(row[0], ":", "direction =", row[1], "(accessible? no)")
  print()


# END OF command5


# executes command6
# prints ridership numbers by month and then asks user if they want to plot it or not
def command6(dbConn):
  print("** ridership by month **")
  dbCursor = dbConn.cursor()

  # querying data
  dbCursor.execute(
    "SELECT strftime('%m', Ride_Date), SUM(Num_Riders) FROM Ridership GROUP BY strftime('%m', Ride_Date)"
  )
  rowRide = dbCursor.fetchall()
  # printing ridership numbers by month
  for row in rowRide:
    print(row[0], ":", f"{row[1]:,}")

  print()
  # plots data
  if input("Plot? (y/n) ") == "y":
    plt.clf()
    x = []
    y = []
    for row in rowRide:  # appending each (x, y) coordinate
      x.append(row[0])
      y.append(row[1])

    plt.xlabel("month")
    plt.ylabel("number of riders (x * 10^8)")
    plt.title("monthly ridership")
    plt.plot(x, y)
    plt.show(block=False)

  print()


# END OF command6


# executes command7
# prints ridership numbers by year and then asks user if they want to plot it or not
def command7(dbConn):
  print("** ridership by year **")
  dbCursor = dbConn.cursor()

  # querying data
  dbCursor.execute(
    "SELECT strftime('%Y', Ride_Date), SUM(Num_Riders) FROM Ridership GROUP BY strftime('%Y', Ride_Date)"
  )
  rowRide = dbCursor.fetchall()
  # printing ridership numbers by year
  for row in rowRide:
    print(row[0], ":", f"{row[1]:,}")

  print()
  # plots data
  if input("Plot? (y/n) ") == "y":
    plt.clf()
    x = []
    y = []
    for row in rowRide:  # appending each (x, y) coordinate
      year = str(row[0])
      yearDigits = year[-2:]
      x.append(yearDigits)
      y.append(row[1])

    plt.xlabel("year")
    plt.ylabel("number of riders (x * 10^8)")
    plt.title("yearly ridership")
    plt.plot(x, y)
    plt.show(block=False)

  print()


# END OF command7


# executes command8
# User inputs a year and the names of two stations (full or partial names), and then outputs the 5 first days and 5 last days of daily ridership at each station for that year.
# Asks user if they want to plot data
def command8(dbConn):
  print()
  dbCursor = dbConn.cursor()

  # station1
  userInputYear = input("Year to compare against? ")
  print()
  userStation1 = input("Enter station 1 (wildcards _ and %): ")
  sqlStation1Amount = "SELECT DISTINCT Station_Name FROM Ridership INNER JOIN Stations ON Ridership.Station_ID = Stations.Station_ID WHERE Station_Name LIKE ?;"
  dbCursor.execute(sqlStation1Amount, [userStation1])
  rowS1Amount = dbCursor.fetchall()

  # checking station 1 query amount and seeing if to get station 2 info
  if len(rowS1Amount) == 0:
    print("**No station found...")
    print()
  elif len(rowS1Amount) > 1:
    print("**Multiple stations found...")
    print()
  else:
    # station 2 input
    print()
    userStation2 = input("Enter station 2 (wildcards _ and %): ")
    sqlStation2Amount = "SELECT DISTINCT Station_Name FROM Ridership INNER JOIN Stations ON Ridership.Station_ID = Stations.Station_ID WHERE Station_Name LIKE ?;"
    dbCursor.execute(sqlStation2Amount, [userStation2])
    rowS2Amount = dbCursor.fetchall()

    # checking station 2 query amount
    if len(rowS2Amount) == 0:
      print("**No station found...")
      print()
    elif len(rowS2Amount) > 1:
      print("**Multiple stations found...")
      print()
    else:
      # querying date, rider amount, Station ID and name based on user input
      sqlStation1 = "SELECT DATE(Ride_Date), SUM(Num_Riders), Ridership.Station_ID, Station_Name FROM Ridership INNER JOIN Stations ON Ridership.Station_ID = Stations.Station_ID WHERE Station_Name LIKE ? AND strftime('%Y', Ride_Date) = ? GROUP BY DATE(Ride_Date) ORDER BY Date(Ride_Date) ASC;"
      dbCursor.execute(sqlStation1, [userStation1, userInputYear])
      rowYearRideS1 = dbCursor.fetchall()
      sqlStation2 = "SELECT DATE(Ride_Date), SUM(Num_Riders), Ridership.Station_ID, Station_Name FROM Ridership INNER JOIN Stations ON Ridership.Station_ID = Stations.Station_ID WHERE Station_Name LIKE ? AND strftime('%Y', Ride_Date) = ? GROUP BY DATE(Ride_Date) ORDER BY Date(Ride_Date) ASC;"
      dbCursor.execute(sqlStation2, [userStation2, userInputYear])
      rowYearRideS2 = dbCursor.fetchall()

      # both stations queried one input successfully so printing info out
      if (len(rowYearRideS1) != 0 and len(rowYearRideS2) != 0):
        # first 5 dates of station1
        for row in range(0, 5):
          if (row == 0):
            print("Station 1:", rowYearRideS1[row][2], rowYearRideS1[row][3])
          print(rowYearRideS1[row][0], rowYearRideS1[row][1])
        # last 5 dates of station1
        for row in range(len(rowYearRideS1) - 5, len(rowYearRideS1)):
          print(rowYearRideS1[row][0], rowYearRideS1[row][1])
        # first 5 dates of station2
        for row in range(0, 5):
          if (row == 0):
            print("Station 2:", rowYearRideS2[row][2], rowYearRideS2[row][3])
          print(rowYearRideS2[row][0], rowYearRideS2[row][1])
        # last 5 dates of station2
        for row in range(len(rowYearRideS2) - 5, len(rowYearRideS2)):
          print(rowYearRideS2[row][0], rowYearRideS2[row][1])

      print()
      # plots data
      if input("Plot? (y/n) ") == "y":
        plt.clf()
        x1 = []  # station 1
        y1 = []
        x2 = []  # station 2
        y2 = []
        # line for station 1
        day = 0
        station1Name = ""
        for row in rowYearRideS1:  # appending  each (x, y) coordinate for station 1
          day = day + 1
          station1Name = row[3]
          x1.append(day)
          y1.append(row[1])

        # line for station 2
        day = 0
        station2Name = ""
        for row in rowYearRideS2:  # appending  each (x, y) coordinate for station 2
          day = day + 1
          station2Name = row[3]
          x2.append(day)
          y2.append(row[1])

        plt.xlabel("day")
        plt.ylabel("number of riders")
        plt.title("riders each day of " + userInputYear)
        plt.xticks([0, 50, 100, 150, 200, 250, 300, 350])
        plt.plot(x1, y1, label=station1Name)
        plt.plot(x2, y2, label=station2Name)
        plt.legend()
        plt.show(block=False)
      print()


# END OF command8


# executes command9
# Outputs all station names with latidude and longitude based on user input color
# asks user if they want to plot or not
def command9(dbConn):
  print()
  dbCursor = dbConn.cursor()
  userInputColor = input("Enter a line color (e.g. Red or Yellow): ")
  # querying data
  sqlColor = "SELECT DISTINCT Stations.Station_Name, Stops.Latitude, Stops.Longitude FROM Stops INNER JOIN Stations ON Stations.Station_ID = Stops.Station_ID INNER JOIN StopDetails ON Stops.Stop_ID = StopDetails.Stop_ID INNER JOIN Lines ON StopDetails.Line_ID = Lines.Line_ID WHERE Lines.Color LIKE ? ORDER BY Stations.Station_Name ASC;"
  dbCursor.execute(sqlColor, [userInputColor])
  rowLines = dbCursor.fetchall()

  # prints all rows relavent to user input
  for row in rowLines:
    if row == "None":
      print("**No such line...")
      break
    print(row[0], ":", f"({row[1]:},", f"{row[2]:})")

  # checks to see if we should ask user about plotting
  if len(rowLines) == 0:
    print("**No such line...")
  else:
    print()
    # plots data
    if input("Plot? (y/n) ") == "y":
      plt.clf()
      x = []  # creates 2 empty vectors/lists
      y = []

      image = plt.imread("chicago.png")
      xydims = [-87.9277, -87.5569, 41.7012,
                42.0868]  # area covered by the map:
      plt.imshow(image, extent=xydims)
      plt.title(userInputColor + " line")
      # color is the value input by user, we can use that to plot the # figure *except* we need to map Purple-Express to Purple:
      if (userInputColor.lower() == "purple-express"):
        userInputColor = "Purple"  # color="#800080"

      plt.plot(x, y, "o", c=userInputColor)

      # annotating each (x, y) coordinate with its station name and appending
      for row in rowLines:
        plt.annotate(row[0], (row[2], row[1]))
        x.append(row[2])
        y.append(row[1])

      plt.plot(x, y, "o", c=userInputColor)
      plt.xlim([-87.9277, -87.5569])
      plt.xticks([-87.9, -87.8, -87.7, -87.6])
      plt.ylim([41.7012, 42.0868])
      plt.show(block=False)
  print()


# END OF command9

##################################################################
#
# main
# setting up program and database
print('** Welcome to CTA L analysis app **')
print()

dbConn = sqlite3.connect('CTA2_L_daily_ridership.db')

print_stats(dbConn)
print()

userInput = input("Please enter a command (1-9, x to exit): ")
# runs program until user exits
while userInput != "x":
  # checking for invalid input
  if len(userInput) != 1:
    print("**Error, unknown command, try again...")
    print()
  elif (not userInput.isdigit() and userInput != "x"):
    print("**Error, unknown command, try again...")
    print()
  elif userInput.isdigit():
    if int(userInput) < 1 or int(userInput) > 9:
      print("**Error, unknown command, try again...")
      print()
    else:
      allCommands(dbConn, userInput)

  userInput = input("Please enter a command (1-9, x to exit): ")
#
# done
#
