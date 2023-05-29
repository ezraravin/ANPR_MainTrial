import mysql.connector
import re

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='LicensePlateRecognition'
)

cursor = db.cursor()
# Fetch Database Value FROM VehicleDB
cursor.execute("SELECT plate_number, vehicle_type FROM VehicleDB")
myResultVehicleDB = cursor.fetchall()
# Fetch Database Value ParkingSystem
cursor.execute("SELECT plate_number, vehicle_type FROM ParkingSystem")
myResultParkingDB = cursor.fetchall()

flagDataMatch = None

# Compare Datas between two tables
# for plateNumberVehicleDB in myResultVehicleDB:
#     for plateNumberParkingDB in myResultParkingDB:
#         if plateNumberVehicleDB == plateNumberParkingDB:
#             flagDataMatch = True
#             break
#         else:
#             flagDataMatch = False

for plateNumberParkingDB in myResultParkingDB:
    if '1255 SSU' == plateNumberParkingDB[0]:
        print("Match")
        flagDataMatch = True
        break
    else:
        print("NO MATCH")
        flagDataMatch = False
print()
print()

if flagDataMatch:
    print("Yes, data exist")
else:
    for plateNumberVehicleDB in myResultVehicleDB:
        strPlateNumberVehicleDB = ''.join(plateNumberVehicleDB[0])
        print(strPlateNumberVehicleDB)


db.commit()

print("Data Read Successfully")
