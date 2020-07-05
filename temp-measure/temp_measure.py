import time
import board
import adafruit_dht
import datetime
from gpiozero import CPUTemperature
import usb
import usb.core
import usb.util


# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D18)
cpu = CPUTemperature()

while True:
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
            str(datetime.datetime.now()).split('.')[0] +"| CPU "+str(cpu.temperature)+" | Ambient: {:.1f} F / {:.1f} C  |  Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            dev = usb.core.find(find_all=True)

            # get next item from the generator
            for d in dev:
                # print (d.get_active_configuration())
                if d._manufacturer is None:
                    try:
                        d._manufacturer = usb.util.get_string(d, d.iManufacturer)
                    except:
                        print("Couldn't find manufacturer id")
                    else:
                        print (str(d._manufacturer))
                if d._product is None:
                    try:
                        d._product = usb.util.get_string(d, d.iProduct)
                    except:
                        print("Couldn't find product id")
                    else:        
                        print (str(d._product))
                print ("++++++++++++++++++++++")
                
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
        print("===================================")
        time.sleep(2.0)
