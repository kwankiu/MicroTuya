from MicroTuya import OutletDevice
import time, ujson

# device list
file_path = "devices.json"

print('---------------------')
print('Welcome to MicroTuya!')
print('---------------------')

# read devices list from file
file = open(file_path, "r")
data = file.read()
print("Reading from " + file_path)
file.close()
data = ujson.loads(data)
dev_list = data['devices']
no_of_dev = len(dev_list)
print(str(no_of_dev) + " devices imported from list")
print('---------------------')

# assigning devices
tuya_device = []
assigned_name = []
assigned_type = []

for i in range(no_of_dev):
    tmp = dev_list[i]
    
    assigned_name.append(tmp["device_name"])
    assigned_type.append(tmp["accessories_type"])
    print("Assigning "+ assigned_name[i] + " as " + assigned_type[i])
    
    tuya_device.append(OutletDevice(tmp["device_id"], tmp["ip_address"], tmp["local_key"]))
    tuya_device[i].set_version(float(tmp["ver"]))

    #print("Device " + str(i))
    #print("Device Name : " + tmp["device_name"])
    print("Device ID : " + tmp["device_id"])
    print("Local Key : " + tmp["local_key"])
    print("IP Address : " + tmp["ip_address"])
    #print("MAC Address : " + tmp["mac_address"])
    #print("Accessories Type : " + tmp["accessories_type"])
    #print("Tuya Protocol Version : " + tmp["ver"])
    print()

if (no_of_dev == len(tuya_device)) :
    print("Sucessfully assigned " + str(no_of_dev) + " devices.")
else :
    print("Only " + len(tuya_device) + "devices assigned, check if there is an error in your file.")


while True:
    print('---------------------')
    print('Which device would you like to control?')
    for i in range(no_of_dev):
        print(str(i+1) + ". " + assigned_name[i])
    d = 0 # init d as 0 so that it runs into input loop
    while (d > no_of_dev) or (d < 1):
        d = int(input("Enter (1-"+str(no_of_dev)+"): "))
    d -= 1 # minus 1 so that it match our list range from 0
    if assigned_type[d] == 'power_strip':
        print('Which switch of ' + assigned_name[d] + ' would you like to control?')
        # TODO : Check how many switch does the device have, and list them all
        which_switch = int(input("Enter (1-4): "))
        s = int(input("ON (1) / OFF (0)?"))
        if s == 1:
            # Turn On
            tuya_device[d].turn_on(which_switch)
        else:
            # Turn Off
            tuya_device[d].turn_off(which_switch)
    else:
        s = int(input("ON (1) / OFF (0)?"))
        if s == 1:
            # Turn On
            tuya_device[d].turn_on()
        else:
            # Turn Off
            tuya_device[d].turn_off()
        

        
    # Output the status
    for i in range(no_of_dev):
        print(tuya_device[i].status())
    print('---------------------')
