from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Serve static files from the 'cesium-project' directory
app.mount("/cesium-project", StaticFiles(directory="cesium-project"), name="cesium_project")


# CORS middleware configuration
origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# run with uvicorn gps_api:app --port 5003 --reload
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
    port=mysql_port
)
cursor = connection.cursor()

@app.get("/")
def render_map_html():
    # Replace 'cesium-project/map.html' with the correct path to your HTML file
    html_file_path = Path("cesium-project/map.html")

    # Check if the file exists
    if html_file_path.exists():
        # Read the content of the HTML file
        html_content = html_file_path.read_text()
        # Use HTMLResponse to serve the HTML content
        return HTMLResponse(content=html_content, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="HTML file not found")

@app.get("/devices")   
def get_devices():
    global cursor
    
    query = "SELECT uuid FROM connected_devices"
    cursor.execute(query)
    devices = cursor.fetchall()
    uuid_list = [device[0] for device in devices]
    return {"devices": uuid_list}

@app.get("/location/{uuid}")
def get_loc_data(uuid: str):
    global cursor
    connection.reconnect()
    query = "SELECT longitude, latitude, altitude FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_3d_coordinates = cursor.fetchone()
    return {"location": device_3d_coordinates}

@app.get("/tdop/{uuid}")
def get_tdop_data(uuid: str):
    global cursor
    
    query = "SELECT tdop, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_tdop_history = cursor.fetchall()
    return {"tdop_history": device_tdop_history}


@app.get("/satellite/{uuid}")
def get_satellite_data(uuid: str):
    global cursor
    query = "SELECT satellites, time FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_satellite_data = cursor.fetchone()
    satellite_list = json.loads(device_satellite_data[0])
    datetime = device_satellite_data[1]
    return {"satellite_list": satellite_list, "datetime": str(datetime)}


@app.get("/prn_satellite_used/{uuid}")
def get_prn_satellite_used(uuid: str):
    global cursor
    
    query = "SELECT satellites, time FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_satellite_data = cursor.fetchone()
    satellite_list = json.loads(device_satellite_data[0])
    datetime = device_satellite_data[1]
    prn_used = []
    for satellite_dict in satellite_list:
        if satellite_dict["used"]:
            prn_used.append(satellite_dict["PRN"])
    return {"prn_satellites_used_array": prn_used, "datetime": str(datetime)}


@app.get("/prn_satellite_seen/{uuid}")
def get_prn_satellite_seen(uuid: str):
    global cursor
        
    query = "SELECT satellites, time FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_satellite_data = cursor.fetchone()
    satellite_list = json.loads(device_satellite_data[0])
    datetime = device_satellite_data[1]
    prn_seen = []
    for satellite_dict in satellite_list:
        prn_seen.append(satellite_dict["PRN"])
    return {"prn_satellites_seen_array": prn_seen, "datetime": str(datetime)}


@app.get("/prn_ss_satellite_used/{uuid}")
def get_prn_ss_satellite_used(uuid: str):
    global cursor
    query = "SELECT satellites, time FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_satellite_data = cursor.fetchone()
    satellite_list = json.loads(device_satellite_data[0])
    datetime = device_satellite_data[1]
    prn_used = []
    for satellite_dict in satellite_list:
        if satellite_dict["used"]:
            prn_used.append({"PRN": satellite_dict["PRN"], "ss": satellite_dict['ss']})
    return {"prn__ss_satellites_used_array": prn_used, "datetime": str(datetime)}


@app.get("/prn_ss_satellite_seen/{uuid}")
def get_prn_ss_satellite_seen(uuid: str):
    global cursor
    query = "SELECT satellites, time FROM gps_data WHERE uuid = %s ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_satellite_data = cursor.fetchone()
    satellite_list = json.loads(device_satellite_data[0])
    datetime = device_satellite_data[1]
    prn_seen = []
    for satellite_dict in satellite_list:
        prn_seen.append({"PRN": satellite_dict["PRN"], "ss": satellite_dict['ss']})
    return {"prn__ss_satellites_used_array": prn_seen, "datetime": str(datetime)}


@app.get("/cpu_temps/{uuid}")
def get_cpu_temps(uuid: str):
    global cursor
    
    query = "SELECT cpu_temp, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_cpu_temps = cursor.fetchall()
    return {"cpu_temps": device_cpu_temps}


@app.get("/cpu_freqs/{uuid}")
def get_cpu_freqs(uuid: str):
    global cursor
    
    query = "SELECT cpu_freq, time FROM gps_data WHERE uuid = %s ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_cpu_freqs = cursor.fetchall()
    return {"cpu_freqs": device_cpu_freqs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("gps_api:app", port=5003, reload=True)
