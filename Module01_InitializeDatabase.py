import mysql.connector


def initializeDatabase():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='LicensePlateRecognition'
    )
    cursor = db.cursor()
    return db, cursor
