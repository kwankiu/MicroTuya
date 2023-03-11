from MicroTuya import OutletDevice

# smart power outlet settings
DEVICE_ID_HERE = ""
IP_ADDRESS = ""
LOCAL_KEY = ""

print("Welcome to MicroTuya!")

# connecting to the power outlet
outlet = OutletDevice(DEVICE_ID_HERE, IP_ADDRESS, LOCAL_KEY)
outlet.setVersion(3.3) # set tuya protocol version to 3.3

outlet.turn_on() # turn on the power outlet
print(outlet.status()) # status of the power outlet
outlet.turn_off() # turn off the power outlet