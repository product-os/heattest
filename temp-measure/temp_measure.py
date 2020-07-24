import time
import board
import adafruit_dht
import datetime
from gpiozero import CPUTemperature
import usb
import usb.core
import usb.util
import subprocess
import csv
from table_logger import TableLogger

timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr)
csvfile = open(timestr+".csv","wb")
tbl = TableLogger(file=csvfile, csv = True,columns='Count,Time,CPU,USB,Freq,Ambient,Humidity')

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D18)
cpu = CPUTemperature()
count = 0
while True:
        count = count + 1
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity

            dev = usb.core.find(find_all=True)

            # get next item from the generator
            sum = 0
            for d in dev:
                sum = sum + 1
                # print (d.get_active_configuration())
                # if d._manufacturer is None:
                #     try:
                #         d._manufacturer = usb.util.get_string(d, d.iManufacturer)
                #     except:
                #         print("Couldn't find manufacturer id")
                #     else:
                #         print (str(d._manufacturer))
                # if d._product is None:
                #     try:
                #         d._product = usb.util.get_string(d, d.iProduct)
                #     except:
                #         print("Couldn't find product id")
                #     else:
                #         print (str(d._product))
                # print ("++++++++++++++++++++++")

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])

        out = subprocess.check_output(["vcgencmd", "measure_clock arm"]).decode("utf-8")
        frequency = float(out.split("=")[1]) / 1000000
        tbl(count, str( datetime.datetime.now()).split('.')[0] ,str(cpu.temperature),str(sum),str(round(frequency)),str(temperature_c),str(humidity))
        print(
                str( datetime.datetime.now()).split('.')[0]
              +"|"+str(cpu.temperature)
              +"|"+str(sum)
              +"|"+str(round(frequency))
              +"|"+str(temperature_c)
              +"|"+str(humidity)
        )
        # print("===================================")
        time.sleep(2.0)
