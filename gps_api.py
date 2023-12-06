from fastapi import FastAPI
import sqlite3

app = FastAPI()
# run with uvicorn gps_api:app --port 5001 --reload

# Establish a connection to the SQLite database
db_file = "gps_test.db"
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

@app.get("/")
def read_root():
    return {"API": "See swagger docs at /docs"}


# Route to send latitude, location, and altitude data
@app.post("/data")
def send_data(latitude: float, location: str, altitude: float):
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


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")