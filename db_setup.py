import sqlite3

# Replace this with the path to your SQLite database file
db_file = "gps_test.db"

# Establish a connection to the SQLite database
connection = sqlite3.connect(db_file)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to create a table
create_device_table_query = """
CREATE TABLE IF NOT EXISTS connected_devices (
    uuid TEXT PRIMARY KEY,
    device_name TEXT,
    datetime DATETIME
)
"""

# Define the SQL query to create a table
create_device_history_query = """
CREATE TABLE IF NOT EXISTS devices_history (
    uuid TEXT PRIMARY KEY,
    device_name TEXT,
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

#SQL query to create a table
create_gps_table_query = """
CREATE TABLE IF NOT EXISTS gps_data (
    time TEXT,
    longitude REAL,
    latitude REAL,
    altitude REAL,
    mode TEXT,
    nSat INTEGER,
    uSat INTEGER,
    TDOP REAL,
    satellites JSON,
    cpu_temp REAL,
    cpu_freq REAL
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
