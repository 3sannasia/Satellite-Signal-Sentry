import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()
# Replace these variables with your MySQL connection details
mysql_user = os.getenv("DB_USER")
mysql_password = os.getenv("DB_PASSWORD")
mysql_host = os.getenv("DB_HOST")
mysql_database = os.getenv("DB_NAME")
mysql_port = os.getenv("DB_PORT")

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user=mysql_user,
    password=mysql_password,
    host=mysql_host,
    database=mysql_database,
    # port = mysql_port
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to create a table
create_device_table_query = """
CREATE TABLE IF NOT EXISTS connected_devices (
    uuid VARCHAR(255) PRIMARY KEY,
    device_name VARCHAR(255),
    datetime DATETIME
)
"""

# Define the SQL query to create a table
create_device_history_query = """
CREATE TABLE IF NOT EXISTS devices_history (
    uuid VARCHAR(255) PRIMARY KEY,
    device_name VARCHAR(255),
    datetime DATETIME
)
"""

drop_device_table_query = """
DROP TABLE IF EXISTS connected_devices
"""

drop_device_history_query = """
DROP TABLE IF EXISTS devices_history
"""

drop_gps_table_query = """
DROP TABLE IF EXISTS gps_data
"""

# SQL query to create a table
create_gps_table_query = """
CREATE TABLE IF NOT EXISTS gps_data (
    uuid VARCHAR(255),
    time VARCHAR(255),
    longitude DOUBLE,
    latitude DOUBLE,
    altitude DOUBLE,
    mode VARCHAR(255),
    nSat INTEGER,
    uSat INTEGER,
    TDOP DOUBLE,
    satellites JSON,
    cpu_temp DOUBLE,
    cpu_freq DOUBLE
)
"""

cursor.execute(drop_device_table_query)
cursor.execute(drop_device_history_query)
cursor.execute(drop_gps_table_query)

cursor.execute(create_device_table_query)
cursor.execute(create_gps_table_query)
cursor.execute(create_device_history_query)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
