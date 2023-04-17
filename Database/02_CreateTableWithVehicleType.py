import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='LicensePlateRecognition'
)

cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE `ParkingSystem` (
        `id` int(11) AUTO_INCREMENT PRIMARY KEY,
        `time_enter` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
        `plate_number` varchar(15) NOT NULL
        `vehicle_type` varchar(15) NOT NULL
    )   
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    """
)

print("Table Created Successfully")
