import mysql.connector
import math
from geopy import distance

# 1.
def getNameandLocation(ICAOcode):
    sql_query = (
        "select ident, airport.name as airport_name, country.name as country_name "
    )
    sql_query += (
        "from airport inner join country on country.iso_country = airport.iso_country "
    )
    sql_query += f"where airport.ident = '{ICAOcode}';"

    cursor = connection.cursor()
    cursor.execute(sql_query)
    response = cursor.fetchall()
    for row in response:
        print(f"Airport name is: {row[1]} and location is {row[2]}")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="dbuser",
    password="pAs5w_0rD",
    autocommit=True,
)

ICAOcode = input("Enter ICAO code of an airport: ")
getNameandLocation00hi(ICAOcode)

# 2.
# def getAirportlist(area_code):
#     sql = "select ident, type, country.name as country_name, count(*) as total from airport "
#     sql += "inner join country on airport.iso_country = country.iso_country "
#     sql += f"where country.iso_country = '{area_code}' group by type;"
#
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     response = cursor.fetchall()
#     result = f"{response[0][2]} has "
#     for row in response:
#         if row[1] == "heliport":
#             result += f"{row[3]} heliport(s), "
#         if row[1] == "small_airport":
#             result += f"{row[3]} small airport(s), "
#         if row[1] == "medium_airport":
#             result += f"{row[3]} medium airport(s), "
#         if row[1] == "large_airport":
#             result += f"{row[3]} large airport(s), "
#         if row[1] == "closed":
#             result += f"{row[3]} closed airport(s), "
#     print(result.rstrip(", "))
#
#
# connection = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     database="flight_game",
#     user="dbuser",
#     password="pAs5w_0rD",
#     autocommit=True,
# )
# area_code = input("Enter the area code: ").upper()
# getAirportlist(area_code)

# 3.
# def calculate_distance(ICAOcode1, ICAOcode2):
#     sql = f"select ident, name, latitude_deg , longitude_deg from airport where ident = '{ICAOcode1}' or ident = '{ICAOcode2}';"
#
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     response = cursor.fetchall()
#     airport1 = response[0][2], response[0][3]
#     airport2 = response[1][2], response[1][3]
#
#     airports_distance = distance.distance(airport1, airport2).km
#     print(
#         f"The distance between {response[0][1]} and {response[1][1]} is {airports_distance:.2f} km"
#     )
#
#
# connection = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     database="flight_game",
#     user="dbuser",
#     password="pAs5w_0rD",
#     autocommit=True,
# )
#
# ICAOcode1 = input("Enter ICAO code of the first airport: ").upper()
# ICAOcode2 = input("Enter ICAO code of the second airport (can not be same as first airport): ").upper()
#
# calculate_distance(ICAOcode1, ICAOcode2)



