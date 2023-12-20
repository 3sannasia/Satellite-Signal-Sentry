# Immersive 3D Visualization: Unveiling the Mystique of GNSS and the Satellites that Power them

The report can be found in the REPORT.md file 


## Installation
- Install Libraries: 
    - ```pip3 install -r requirements.txt```
- Setup MySQL instance and .env file
- Run Database Setup file
    - ```python3 db_setup.py```
- Run Project (api service + GNSS receiver data collection + frontend) 
    - run ```./run_gps_api.sh```

## Usage
- Need a .env file with your mysql database credentials
- Obtain device with a GNSS reciever with an active fix and running GPSD
- On running the backend your device
    - automatically registers itself to MySQL 
    - uploads data to our MySQL instance
- On shutting down the backend
    - device unregisters from active devices table on MySQL
    - device stays recorded in the connected_devices_history table
- The CesiumJS frontend uses the data to populate the globe with device locations and satellites in real-time
- ChartJS charts are displayed
    - cpu temperatures over time
    - cpu frequency over time
    - TDOP (time dilution of precision) over time
    - current satellite signal strength

### Features
1. 3D Visualization of gps locations on the Earth
2. Satellites orbitting the Earth in real-time
3. See what satellites your gps device is using
4. Click on device location or name to be redirected to generated graphs of cpu-temp, cpu-freq, TDOP (time dilution of precision), and used satellite PRN and their satellite strengths
### Testing
- run ```./run_gps_api.sh```
- Navigate to the FastAPI docs ```http://127.0.0.1:5003/docs```



## People
- Akash Sannasi
- Harshda Ghai
- Ananya Agarwal
- Vashishth Goswami



