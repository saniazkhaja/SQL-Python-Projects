
#
# objecttier
#
# Builds objects from data retrieved through the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#
import datatier
#
# do not import other modules
#

########################################################
#
# Station:
#
# Constructor(...)
# Properties:
#   Station_ID: int
#   Station_Name: string
#   Ridership: int
#   Percent_Ridership: float
#
class Station:
  def __init__(self, id, name, riders, percent):
    self._Station_ID = id
    self._Station_Name = name
    self._Ridership = riders
    self._Percent_Ridership = percent
    
  @property
  def Station_ID(self):
    return self._Station_ID

  @property
  def Station_Name(self):
    return self._Station_Name

  @property
  def Ridership(self):
    return self._Ridership

  @property
  def Percent_Ridership(self):
    return self._Percent_Ridership

########################################################
#
# Stop:
#
# Constructor(...)
# Properties:
#   Stop_ID: int
#   Stop_Name: string
#   Direction: string
#   Accessible: boolean (True/False)
#   Latitude: float
#   Longitude: float
#   Lines: list of strings
#
class Stop:
  def __init__(self, id, name, direction, access, lat, long, line):
    self._Stop_ID = id
    self._Stop_Name = name
    self._Direction = direction
    self._Accessible = access
    self._Latitude = lat
    self._Longitude = long
    self._Lines = line
    
  @property
  def Stop_ID(self):
    return self._Stop_ID

  @property
  def Stop_Name(self):
    return self._Stop_Name

  @property
  def Direction(self):
    return self._Direction

  @property
  def Accessible(self):
    return self._Accessible

  @property
  def Latitude(self):
    return self._Latitude

  @property
  def Longitude(self):
    return self._Longitude

  @property
  def Lines(self):
    return self._Lines


########################################################
#
# get_stations:
#
# gets and returns all stations whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of stations in ascending order by name;
#          returns None if an error occurs.
#
def get_stations(dbConn, pattern):
  sql = "SELECT Stations.Station_ID, Stations.Station_Name, SUM(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID WHERE Station_Name LIKE ? GROUP BY Station_Name ORDER BY Station_Name ASC;"
  sqlTotalRiders = "SELECT SUM(Num_Riders) FROM Ridership;"
  rowStationNames = datatier.select_n_rows(dbConn, sql, [pattern])
  rowTotalRiders = datatier.select_one_row(dbConn, sqlTotalRiders)

  if rowStationNames is None or len(rowStationNames) == 0:
    return []
  else:
    list = [];
    for row in rowStationNames:
      objectStation = Station(row[0], row[1], row[2], (row[2] / rowTotalRiders[0]) * 100)
      list.append(objectStation)
    return list
      


########################################################
#
# get_stops:
#
# gets and returns all stops at a given station; the 
# given station name must match exactly (no wildcards).
# If there is no match, an empty list is returned.
#
# Returns: a list of stops in ascending order by name,
#          then in ascending order by id if two stops
#          have the same name; returns None if an error
#          occurs.
#
def get_stops(dbConn, name):
  sql = "SELECT Stops.Stop_ID, Stops.Stop_Name, Stops.Direction, Stops.ADA, Stops.Latitude, Stops.Longitude, Lines.Color FROM Stops INNER JOIN Stations ON Stations.Station_ID = Stops.Station_ID INNER JOIN StopDetails ON Stops.Stop_ID = StopDetails.Stop_ID INNER JOIN Lines ON StopDetails.Line_ID = Lines.Line_ID WHERE Stations.Station_Name = ? ORDER BY Stop_Name ASC;"
  rowStopNames = datatier.select_n_rows(dbConn, sql, [name])

  if rowStopNames is None or len(rowStopNames) == 0:
    return []
  else:
    list = []
    colorsList = []
    for row in range (0, len(rowStopNames)):
      if (row < len(rowStopNames) - 1 and rowStopNames[row][0] == rowStopNames[row+1][0]):
        colorsList.append(rowStopNames[row][6])
      else:
        colorsList.append(rowStopNames[row][6])
        colorsList.sort()
        objectStation = Stop(rowStopNames[row][0], rowStopNames[row][1], rowStopNames[row][2], rowStopNames[row][3], rowStopNames[row][4], rowStopNames[row][5], colorsList)
        list.append(objectStation)
        colorsList = []
    return list
