from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

app = FastAPI()

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
cursor = connection.cursor()

@app.get("/")
def read_root():
    return {"message": "See swagger docs at /docs"}

@app.get("/devices")   
def get_devices():
    # Use the existing MySQL cursor
    global cursor
    
    query = "SELECT uuid FROM connected_devices"
    cursor.execute(query)
    devices = cursor.fetchall()
    uuid_list = [device[0] for device in devices]
    return {"devices": uuid_list}

@app.get("/location/{uuid}")
def get_loc_data(uuid: str):
    global cursor
    
    query = "SELECT longitude, latitude, altitude FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_3d_coordinates = cursor.fetchone()
    print(device_3d_coordinates)
    return {"location": device_3d_coordinates}

@app.get("/tdop/{uuid}")
def get_tdop_data(uuid: str):
    global cursor
    
    query = "SELECT tdop, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_tdop_history = cursor.fetchall()
    print(device_tdop_history)
    return {"tdop_history": device_tdop_history}

@app.get("/satellite/{uuid}")
def get_satellite_data(uuid: str):
    query = "SELECT satellites, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_satellite = cursor.fetchall()
    print(device_satellite)
    return {"device_satellite": device_satellite}

@app.get("/cpu_temps/{uuid}")
def get_cpu_temps(uuid: str):
    global cursor
    
    query = "SELECT cpu_temp, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_cpu_temps = cursor.fetchall()
    print(device_cpu_temps)
    return {"cpu_temps": device_cpu_temps}

@app.get("/cpu_freqs/{uuid}")
def get_cpu_freqs(uuid: str):
    global cursor
    
    query = "SELECT cpu_freq, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_cpu_freqs = cursor.fetchall()
    print(device_cpu_freqs)
    return {"cpu_freqs": device_cpu_freqs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("gps_api:app", host="127.0.0.1", port=5001, reload=True)
