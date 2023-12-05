import gpsd
import time
import psutil
from gpiozero import CPUTemperature

def get_gps_info():
    # Connect to the local GPSD service (assuming it's running on localhost)
    gpsd.connect()
    print(gpsd.device()) # for debugging port
    
    # Get the GPSD data stream
    packet = gpsd.get_current()
    
    # Print some basic information
    print("Time (UTC):", packet.time)
    print("Latitude:", packet.lat)  #requires mode >=2
    print("Longitude:", packet.lon) #requires mode >=2
    print("Altitude:", packet.alt) #requires mode >=3
    print("Mode: " + str(packet.mode))
    print("Satellites Seen: " + str(packet.sats))  
    print("Satellites Seen (Valid): " + str(packet.sats_valid))  
    # I want TDOP



if __name__ == "__main__":
    try:
        
        while True:
            time.sleep(2)  # Wait for 5 seconds before getting the next update
            
            get_gps_info()
            
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

