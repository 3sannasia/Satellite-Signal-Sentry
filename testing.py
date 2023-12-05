import gps
import time
import psutil
from gpiozero import CPUTemperature
import mysql.connector
import sqlite3
import uuid
import datetime

#https://gpsd.gitlab.io/gpsd/gpsd_json.html#_sky
# Data attributes and descriptions in link above


running = True
uuid = str(uuid.uuid4())
print("UUID: " + uuid)


# Establish a connection to the SQLite database
db_file = "gps_test.db"
connection = sqlite3.connect(db_file)
cursor = connection.cursor()


def register_to_database():
    device_json = {
        'uuid': str(uuid),
        'device_name': 'Raspberry Pi 4',
        'datetime': str(datetime.datetime.now())
    }
    register_insert_query = "INSERT INTO connected_devices (uuid, device_name, datetime) VALUES (?, ?, ?)"
    cursor.execute(register_insert_query, (device_json['uuid'], device_json['device_name'], device_json['datetime']))
    connection.commit()
    
    print("Device registered to database!")
    
def unregister_from_database():
    unregister_query = "DELETE FROM connected_devices WHERE uuid = ?"
    cursor.execute(unregister_query, (uuid))
    connection.commit()
    
    print("Device unregistered from database!")
register_to_database()
unregister_from_database()

def get_TPV_SKY_data(gps):
    nx = gps.next()
    
    if nx['class'] == 'TPV':
        if hasattr(nx, 'time'):
            print("Time: ", nx.time)
        if hasattr(nx, 'lon'):
            print("Longitude: ", nx.lon)
        if hasattr(nx, 'lat'):
            print("Latitude: ", nx.lat)
        if hasattr(nx, 'alt'):
            print("Altitude: ", nx.alt, 'm')
        if hasattr(nx, 'mode'):
            print("Mode: ", nx.mode)
            
   
    if nx['class'] == 'SKY':
        if hasattr(nx, 'satellites'):
            for satellite_info in nx.satellites:
                print("Satellite: ", satellite_info)
                 
        if hasattr(nx, 'tdop'): #time dilution based on satellite position
            print("TDOP: ", nx.tdop)
        if hasattr(nx, 'nSat'):
            print("Satellites Seen:", nx.nSat)
        if hasattr(nx, 'uSat'):
            print("Satellites Used:", nx.uSat)
        
    
    
def get_cpu_frequency():
    # Get CPU frequency in Hz
    frequency = psutil.cpu_freq().current
    return frequency

def get_device_temperature():
    # Get Raspberry Pi temperature in Celsius
    cpu_temp = CPUTemperature().temperature
    return cpu_temp

        
            


# gpsd = gps.gps(mode=gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)

# try:
#     print("Application started!")
#     while running:
#         get_TPV_SKY_data(gpsd)
#         print(str(get_cpu_frequency()) + " Hz")
#         print(str(get_device_temperature()) + " C")
#         print("\n---\n")
#         time.sleep(2)
# except KeyboardInterrupt:
#     running = False
#     print("Applications closed!")