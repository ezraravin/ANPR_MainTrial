import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='LicensePlateRecognition'
)

cursor = db.cursor()
query = "INSERT INTO ParkingSystem(plate_number) VALUES (%s)"
plateNumberData = ("D 163 IV")
cursor.execute(query, plateNumberData)

db.commit()

print("Data Added Successfully")
