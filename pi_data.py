import gps
import time
import psutil
from gpiozero import CPUTemperature
import mysql.connector
import sqlite3
import uuid
import datetime
import json
import platform

#https://gpsd.gitlab.io/gpsd/gpsd_json.html#_sky
# Data attributes and descriptions in link above

gpsd = gps.gps(mode=gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)

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
        'device_name': platform.uname().node + ": " + platform.machine(),
        'datetime': str(datetime.datetime.now())
    }
    register_insert_query = "INSERT INTO connected_devices (uuid, device_name, datetime) VALUES (?, ?, ?)"
    cursor.execute(register_insert_query, (device_json['uuid'], device_json['device_name'], device_json['datetime']))
    connection.commit()
    
    print("Device registered to database!")
    
    
def unregister_from_database():
    unregister_query = "DELETE FROM connected_devices WHERE uuid = ?"
    cursor.execute(unregister_query, (uuid,))
    connection.commit()
    
    print("Device unregistered from database!")

    
def get_TPV_SKY_device_data(gps):
    time = None
    longitude = None
    latitude = None
    altitude = None
    mode = None
    tdop = None
    nSat = None
    uSat = None
    satellites = None

      
    nx = gps.next()
    while nx['class'] != 'TPV':
        nx = gps.next()

    nx2 = gps.next()
    while nx2['class'] != 'SKY':
        nx2 = gps.next()
        
    if nx['class'] == 'TPV':
        if hasattr(nx, 'time'):
            # print("Time: ", nx.time)
            time = nx.time
        if hasattr(nx, 'lon'):
            # print("Longitude: ", nx.lon)
            longitude = nx.lon
        if hasattr(nx, 'lat'):
            # print("Latitude: ", nx.lat)
            latitude = nx.lat
        if hasattr(nx, 'alt'):
            # print("Altitude: ", nx.alt, 'm')
            altitude = nx.alt
        if hasattr(nx, 'mode'):
            mode = nx.mode
            # print("Mode: ", nx.mode)
            
   
    if nx2['class'] == 'SKY':
        if hasattr(nx2, 'satellites'):
            satellites = nx2.satellites
            test_sat = []
            for satellite_info in nx2.satellites:
                # print("Satellite: ", satellite_info)
                test_sat.append(dict(satellite_info))
                 
        if hasattr(nx2, 'tdop'): #time dilution based on satellite position
            # print("TDOP: ", nx2.tdop)
            tdop = nx2.tdop
        if hasattr(nx2, 'nSat'):
            # print("Satellites Seen:", nx2.nSat)
            nSat = nx2.nSat
        if hasattr(nx2, 'uSat'):
            uSat = nx2.uSat
            # print("Satellites Used:", nx2.uSat)
    insert_GPS_data(time, longitude, latitude, altitude, mode, tdop, nSat, uSat, json.dumps(test_sat), get_device_temperature(), get_cpu_frequency())
 

def get_cpu_frequency():
    # Get CPU frequency in Hz
    frequency = psutil.cpu_freq().current
    return frequency

def get_device_temperature():
    # Get Raspberry Pi temperature in Celsius
    cpu_temp = CPUTemperature().temperature
    return cpu_temp


def insert_GPS_data(time, longitude, latitude, altitude, mode, tdop, nSat, uSat, satellites, cpu_temp, cpu_freq):
    gps_json = {
        'time': time,
        'longitude': longitude,
        'latitude': latitude,
        'altitude': altitude,
        'mode': mode,
        'nSat': nSat,
        'uSat': uSat,
        'TDOP': tdop,
        'satellites': satellites,
        'cpu_temp': cpu_temp,
        'cpu_freq': cpu_freq
    }
    gps_insert_query = "INSERT INTO gps_data (time, longitude, latitude, altitude, mode, nSat, uSat, TDOP, satellites, cpu_temp, cpu_freq) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(gps_insert_query, (gps_json['time'], gps_json['longitude'], gps_json['latitude'], gps_json['altitude'], gps_json['mode'], gps_json['nSat'], gps_json['uSat'], gps_json['TDOP'], gps_json['satellites'], gps_json['cpu_temp'], gps_json['cpu_freq']))
    connection.commit()
    print("\nGPS data inserted to database!")
    
    
def print_TPV_SKY_data(gps):
    
    nx = gps.next()

    while nx['class'] != 'TPV':
        nx = gps.next()

    nx2 = gps.next()

    while nx2['class'] != 'SKY':
        nx2 = gps.next()
        
    print(nx['class'])
    print(nx2['class'])
    
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
            
    print(nx2['class'])
    if nx2['class'] == 'SKY':
        print("Satellites: ")
        if hasattr(nx2, 'satellites'):
            for satellite_info in nx2.satellites:
                print("Satellite: ", dict(satellite_info))
                 
        if hasattr(nx2, 'tdop'): #time dilution based on satellite position
            print("TDOP: ", nx2.tdop)
        if hasattr(nx2, 'nSat'):
            print("Satellites Seen:", nx2.nSat)
        if hasattr(nx2, 'uSat'):
            print("Satellites Used:", nx2.uSat)
            
    print(str(get_cpu_frequency()) + " Hz")
    print(str(get_device_temperature()) + " C")
    
    print("\n-----------------------------------------------------\n")
    


try:
    register_to_database()
    print("GPS Application Started!")
    while running:
        print_TPV_SKY_data(gpsd)
        get_TPV_SKY_device_data(gpsd)
        time.sleep(2)
except KeyboardInterrupt:
    running = False
    print('\n')
    unregister_from_database()
    
    print("GPS closed!")