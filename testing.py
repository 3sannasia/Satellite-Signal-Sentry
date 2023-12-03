import gps
import time

running = True

def getPositionData(gps):
    nx = gpsd.next()
    print(nx['class'])
    # import pdb; pdb.set_trace()
    
    if nx['class'] == 'TPV':
        if hasattr(nx, 'time'):
            print("Time: ", nx.time)
        if hasattr(nx, 'lon'):
            print("Longitude: ", nx.lon)
        if hasattr(nx, 'lat'):
            print("Latitude: ", nx.lat)
        if hasattr(nx, 'alt'):
            print("Altitude: ", nx.alt, 'm')
        if hasattr(nx, 'speed'):
            print("Speed: ", nx.speed, 'm/s')
        if hasattr(nx, 'climb'):
            print("Climb: ", nx.climb, 'm/s')
        if hasattr(nx, 'track'):
            print("Track: ", nx.track, 'degrees')
        if hasattr(nx, 'mode'):
            print("Mode: ", nx.mode)
    if nx['class'] == 'SKY':
        if hasattr(nx, 'satellites'):
            print("Satellites: ", nx.satellites)
        if hasattr(nx, 'satellites_visible'):
            print("\n working \n")
            print("Satellites Visible: ", nx.satellites_visible)
        if hasattr(nx, 'hdop'):
            print("HDOP: ", nx.hdop)
        if hasattr(nx, 'vdop'):
            print("VDOP: ", nx.vdop)
        if hasattr(nx, 'pdop'):
            print("PDOP: ", nx.pdop)
        if hasattr(nx, 'gdop'):
            print("GDOP: ", nx.gdop)
        if hasattr(nx, 'tdop'):
            print("TDOP: ", nx.tdop)
        if hasattr(nx, 'mode'):
            print("Mode: ", nx.mode)
    # if nx['class'] == 'ATT':
    #     if hasattr(nx, 'heading'):
    #         print("Heading: ", nx.heading)
    #     if hasattr(nx, 'mag_st'):
    #         print("Magnetic Variation: ", nx.mag_st)
    #     if hasattr(nx, 'pitch'):
    #         print("Pitch: ", nx.pitch)
    #     if hasattr(nx, 'yaw'):
    #         print("Yaw: ", nx.yaw)
            


gpsd = gps.gps(mode=gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)

try:
    print("Application started!")
    while running:
        getPositionData(gpsd)
        time.sleep(1)
except KeyboardInterrupt:
    running = False
    print("Applications closed!")