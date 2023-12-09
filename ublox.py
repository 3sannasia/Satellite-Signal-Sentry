from pyubx2 import UBXReader, UBXMessage, SET
import serial
ubx_reader = UBXReader()


#Remember to replace the placeholder values with the correct values for your specific use case. Always refer to the u-blox documentation for your specific module version to get accurate information about the UBX message formats and parameters. Additionally, consider handling exceptions and errors appropriately in your code.


serial_port = serial.Serial('tty/ACM0', 9600)  # Change 'COM1' to your actual serial port
cfg_gnss_message = UBXMessage("CFG", "CFG-GNSS", SET)


cfg_gnss_message.add('msgVer', 0)  # Change these values based on the UBX-CFG-GNSS format
cfg_gnss_message.add('numTrkChHw', 16)
cfg_gnss_message.add('numTrkChUse', 16)
cfg_gnss_message.add('numConfigBlocks', 1)

# Add configuration for the first GNSS block
cfg_gnss_message.add('gnssId', 0)  # GNSS identifier (0 for GPS)
cfg_gnss_message.add('resTrkCh', 4)  # Number of reserved tracking channels
cfg_gnss_message.add('maxTrkCh', 16)  # Maximum number of tracking channels

# Set the flags field to use only USA GPS satellites
cfg_gnss_message.add('flags', 0x01)  # Set the flag to use USA GPS satellites



ubx_message_bytes = cfg_gnss_message.serialize()
serial_port.write(ubx_message_bytes)


serial_port.close()

