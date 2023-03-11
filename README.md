# MicroTuya
Controlling Tuya smart devices using MicroPython locally over LAN

# Status
- Currently only support ESP32 (Tell me if you found it working on another device, so that i can add it here)
- Tested to work with ESP32-C3 
- Tested to be able to control Smart Plug and Smart Power Strip from Globe (Should works on other Tuya devices that use WiFi)

NOTE : For those who want to use this with ESP8266, I have tested it which resulted in MemoryError: memory allocation failed. (Tell to me if you got a way to get it working)

# Quickstart : Example 1 - Add & Control devices from JSON list

This Example reads a device list we created from a JSON File, assign them and control them by user input (via Serial Monitor).

NOTE : You must first have your Tuya device setup with Smart Life App or Tuya Smart App.

## 1. Download and copy everything in /lib to the /lib of your MicroPython device.

## 2. Copy multi-device-from-json.py and devices.json to your MicroPython parent directory.

## 3. Setup and Connect our MicroPython device to WiFi

Add the following code to your `boot.py` (if boot.py does not exist, create a file named boot.py)

```
import network

ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
```

Dont forget to define WiFi SSID and Password by modifying this two line:
```
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'
```

## 4. Let's open devices.json and see what we have.

NOTE :

Controlling and monitoring Tuya devices on your network requires the following:

- IP_ADDRESS - The network address (IPv4) of the device e.g. 192.168.1.123
- DEVICE_ID - The unique identifier for the Tuya device
- VERSION - The Tuya protocol version used (3.1 or 3.3)
- LOCAL_KEY - The security key required to access the Tuya device. 

You will need to register an account and create a project on Tuya IoT to get your LOCAL_KEY.

```
{
    "devices": [
        {
            "device_name": "Bedroom Lamp",
            "device_id": "YOUR_DEVICE_ID",
            "local_key": "YOUR_LOCAL_KEY",
            "ip_address": "192.168.1.123",
            "mac_address": "aa:bb:cc:dd:ee:f1",
            "accessories_type": "plug",
            "ver": "3.3"
        },
        {
            "device_name": "Oven",
            "device_id": "YOUR_DEVICE_ID",
            "local_key": "YOUR_LOCAL_KEY",
            "ip_address": "192.168.1.124",
            "mac_address": "aa:bb:cc:dd:ee:f2",
            "accessories_type": "plug",
            "ver": "3.3"
        },
        {
            "device_name": "Smart Power Strip",
            "device_id": "YOUR_DEVICE_ID",
            "local_key": "YOUR_LOCAL_KEY",
            "ip_address": "192.168.1.125",
            "mac_address": "aa:bb:cc:dd:ee:f3",
            "accessories_type": "power_strip",
            "ver": "3.3"
        }
    ]
}
```

From this sample, you can add your device's infomation inside `devices`.

Now modify this file to match your Tuya device's infomation.

### Configuration reference

`device_name` : Give your device a name, this can be anything you would like your device to be called.

`device_id` : The unique identifier for the Tuya device, you can get this from Tuya Smart App.

`local_key` : The Local Key that allows us to communicate with the device over LAN, you can retrieve this from Tuya IoT Platform.

`ip_address` : The Local IP Address of your Tuya device assigned by your Router, this is important to communicate with your device locally.

`mac_address` : The MAC Address of your Tuya device, you can get this either from Tuya Smart App or your Router's client list (You may also be able to get this from a LAN Network Scanner), this is currently optional, but maybe useful to have it in case your device's local ip address has been re-assigned.

`accessories_type` : This allows us to determine what accessory is our Tuya Devices, currently supported type are :

        'plug' - single on/off control
        
        'power_strip' - multiple on/off control.

`ver` : The protocol version of your Tuya device, currently supported version are `3.1` and `3.3`.

## 4. Once you have your device list json file ready, you can run `multi-device-from-json.py` and start controlling your Tuya device.

# Usage

NOTE : You must first have your Tuya device setup with Smart Life App or Tuya Smart App.

## 1. Download and copy everything in /lib to the /lib of your MicroPython device.

## 2. Import this library to your program.

```
from MicroTuya import OutletDevice
```

## 3. Setup and Connect our MicroPython device to WiFi

Add the following code to your `boot.py` (if boot.py does not exist, create a file named boot.py)

```
import network

ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
```

Dont forget to define WiFi SSID and Password by modifying this two line:
```
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'
```

## 4. Add a device. 

Controlling and monitoring Tuya devices on your network requires the following:

- IP_ADDRESS - The network address (IPv4) of the device e.g. 192.168.1.123
- DEVICE_ID - The unique identifier for the Tuya device
- VERSION - The Tuya protocol version used (3.1 or 3.3)
- LOCAL_KEY - The security key required to access the Tuya device. 

NOTE : You will need to register an account and create a project on Tuya IoT to get your LOCAL_KEY

Now, we can assign a device.

```
outlet = OutletDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)
```

Then, we need to set the Tuya protocol version (for example, 3.3)

```
outlet.set_version(3.3)
```

## 5. Controlling the device.

To Turn ON the device,
```
outlet.turn_on()
```

To Turn OFF the device,
```
outlet.turn_off()
```
## 6. Get device status
```
outlet.status()
```

This is a sample of the output :
```
{'dps': {'1': False, '9': 0}, 'devId': '123456789abcdef'}
```

- `'dps'` - the status returned from the device
- `'1': False` - this means Switch 1 of the device is TURNED OFF. If the device is a power strip, there can be more than 1 switch.
- `'devId'` : the DEVICE_ID of the requested device

# More Information


# Acknowledgements
* This project is based on: https://github.com/lemariva/SmartUPy (which is based on: https://github.com/clach04/python-tuya)
