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
@app.post("/location{uuid}")
def send_loc_data(latitude: float, location: str, altitude: float):
    # Process and store the data
    
    # ...
    return {"message": "Data received successfully"}

# Route to send TDOP data for each UUID device over time
@app.post("/tdop/{uuid}")
def send_tdop_data(uuid: str, tdop: float):
    # Process and store the TDOP data for the specified UUID
    # ...
    return {"message": f"TDOP data received for UUID: {uuid}"}

# Route to send the latest satellite data for a specific device
@app.get("/satellite/{uuid}")
def get_satellite_data(uuid: str):
    # Retrieve and return the latest satellite data for the specified UUID
    # ...
    return {"message": f"Satellite data for UUID: {uuid}"}

@app.get("/cpu_temps/{uuid}")
def get_cpu_temps(uuid: str):
    # Retrieve and return the latest temperature data for the specified UUID
    # ...
    return {"message": f"Temperature data for UUID: {uuid}"}

@app.get("/cpu_freqs/{uuid}")
def get_cpu_freqs(uuid: str):
    # Retrieve and return the latest pressure data for the specified UUID
    # ...
    return {"message": f"Pressure data for UUID: {uuid}"}


if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=5001) # production
    import uvicorn
    uvicorn.run("gps_api:app", host="127.0.0.1", port=5001, reload=True)
    