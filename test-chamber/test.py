import time
import board
import digitalio

print("hello blinka!")

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT


while True:
        led.value = 0
        time.sleep(100)
        led.value = 1
        time.sleep(100)
