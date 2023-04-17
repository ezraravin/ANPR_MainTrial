import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='LicensePlateRecognition'
)

cursor = db.cursor()
query = "INSERT INTO ParkingSystem(plate_number, vehicle_type) VALUES (%s, %s)"
plateNumberData = ("D 163 IV", "Car")
cursor.execute(query, plateNumberData)

db.commit()

print("Data Added Successfully")
