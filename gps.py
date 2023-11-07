import serial
import pynmea2

# Configure the serial connection settings
port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)

while True:
    try:
        newdata = ser.readline().decode('ascii', errors='replace')

        if newdata.startswith('$GPGGA'):
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = f"Latitude={lat} and Longitude={lng}"
            print(gps)

    except serial.SerialException as e:
        print(f"Error reading from the serial port: {e}")
    except pynmea2.ParseError as e:
        print(f"Error parsing NMEA sentence: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        break

ser.close()
