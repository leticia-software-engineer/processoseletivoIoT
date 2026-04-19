from machine import Pin
import time

leds = [
    Pin(22, Pin.OUT),  # vermelho
    Pin(19, Pin.OUT),  # amarelo
    Pin(4, Pin.OUT)    # verde
]

def apagar_todos():
    for led in leds:
        led.value(0)

def acender(led, tempo):
    apagar_todos()
    led.value(1)
    time.sleep(tempo)

# estado inicial
apagar_todos()

while True:
    acender(leds[0], 5)
    acender(leds[2], 5)
    acender(leds[1], 2)