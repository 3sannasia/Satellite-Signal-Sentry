from fastapi import FastAPI

app = FastAPI()

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

