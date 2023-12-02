import gpsd
import time
import psutil
from gpiozero import CPUTemperature

def get_gps_info():
    # Connect to the local GPSD service (assuming it's running on localhost)
    gpsd.connect()
    print(gpsd.device())
    

    # Get the GPSD data stream
    packet = gpsd.get_current()
    

    # Print some basic information
    print("Time (UTC):", packet.time)
    print("Latitude:", packet.lat)  #requires mode >=2
    print("Longitude:", packet.lon) #requires mode >=2
    print("Altitude:", packet.alt) #requires mode >=3
    print("Mode: " + str(packet.mode))
    print("Satellites Seen: " + str(packet.sats))  
    print(CPUTemperature().temperature, "Celsius")
    print(psutil.cpu_freq().current, "Hz")
    
 

if __name__ == "__main__":
    try:
        
        while True:
            get_gps_info()
            print("\n---\n")
            time.sleep(5)  # Wait for 5 seconds before getting the next update
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

