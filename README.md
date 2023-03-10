# MicroTuya
Controlling Tuya smart devices using MicroPython locally over LAN

# Status
- Currently only support ESP32 (Please report to me if you found it working on another device, so that i can add it here)
- Tested to work with ESP32-C3 
- Tested to be able to control Smart Plug and Smart Power Strip from Globe (Should works on other Tuya devices that use WiFi)

# Usage

NOTE : You must first have your Tuya device setup with Smart Life App or Tuya Smart App.

## 1. Download and copy everything in /lib to the /lib of your MicroPython device.

## 2. Import this library to your program.

```
from MicroTuya import OutletDevice
```

## 3. Setup WiFi for our MicroPython device

First, we can define a function do_connect() which connect our device to WiFi :
```
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi_ssid, wifi_password)
        while not sta_if.isconnected():
            pass
    print('Network configured as follow:', sta_if.ifconfig())
```

Dont forget to define wifi_ssid and wifi_password:
```
wifi_ssid = 'YOUR SSID'
wifi_password = 'YOUR_PASSWORD'
```

Now, run do_connect() in your main program :
```
do_connect()
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
