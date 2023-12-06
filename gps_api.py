from fastapi import FastAPI
import sqlite3

app = FastAPI()
# run with uvicorn gps_api:app --port 5001 --reload

# Establish a connection to the SQLite database


@app.get("/")
def read_root():
    return {"message": "See swagger docs at /docs"}

@app.get("/devices")   
def get_devices():
    db_file = "gps_test.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    query = "SELECT uuid FROM connected_devices"
    cursor.execute(query)
    devices = cursor.fetchall()
    uuid_list = []
    for device in devices:
        uuid_list.append(device[0])
    return {"devices": uuid_list}

# Route to send latitude, location, and altitude data
# 761db5b1-7a34-4952-b4c1-d8b3c2e253aa
@app.get("/location/{uuid}")
def get_loc_data(uuid: str):
    db_file = "gps_test.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    query = "SELECT longitude, latitude, altitude FROM gps_data WHERE uuid = ? ORDER BY time DESC LIMIT 1"
    cursor.execute(query, (uuid,))
    device_3d_coordinates = cursor.fetchone()
    print(device_3d_coordinates)
    # ...
    return {"location": device_3d_coordinates}

# Route to send TDOP data for each UUID device over time
@app.get("/tdop/{uuid}")
def get_tdop_data(uuid: str):
    db_file = "gps_test.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    query = "SELECT tdop, time FROM gps_data WHERE uuid = ? ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_tdop_history = cursor.fetchall()
    print(device_tdop_history)
    # ...
    return {"tdop_history": device_tdop_history}

# Route to send the latest satellite data for a specific device
@app.get("/satellite/{uuid}")
def get_satellite_data(uuid: str):
    # Retrieve and return the latest satellite data for the specified UUID
    # ...
    db_file = "gps_test.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    query = "SELECT satellite, time FROM gps_data WHERE uuid = ? ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_satellite = cursor.fetchall()
    print(device_satellite)
    # ...
    return {"device_satellite": device_satellite}

@app.get("/cpu_temps/{uuid}")
def get_cpu_temps(uuid: str):
    # Retrieve and return the latest temperature data for the specified UUID
    # ...
    db_file = "gps_test.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    query = "SELECT cpu_temp, time FROM gps_data WHERE uuid = ? ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_cpu_temps = cursor.fetchall()
    print(device_cpu_temps)
    # ...
    return {"cpu_temps": device_cpu_temps}

@app.get("/cpu_freqs/{uuid}")
def get_cpu_freqs(uuid: str):
    db_file = "gps_test.db"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    query = "SELECT cpu_freq, time FROM gps_data WHERE uuid = ? ORDER BY time DESC"
    cursor.execute(query, (uuid,))
    device_cpu_freqs = cursor.fetchall()
    print(device_cpu_freqs)
    # ...
    return {"cpu_freqs": device_cpu_freqs}


if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=5001) # production
    import uvicorn
    uvicorn.run("gps_api:app", host="127.0.0.1", port=5001, reload=True)
    