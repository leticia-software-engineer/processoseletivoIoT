from machine import Pin
import time

leds = [
    Pin(22, Pin.OUT),  # vermelho
    Pin(19, Pin.OUT),  # amarelo
    Pin(4, Pin.OUT)    # verde
]

def apagar_todos(): #Função que inicializa os leds apagados
    for led in leds:
        led.value(0) #Configura o estado baixo

def acender(led, tempo): #Função que acende o led na sua vez
    apagar_todos() #Apaga os leds acesos antes de acender outro led, evitando que dois leds brilhem simultaneamente
    led.value(1) #Configura o estado alto do led
    time.sleep(tempo) #Define um delay configurável para que o led fique aceso

# Chama a função de estado inicial
apagar_todos()

#Funciona em loop infinito, sem necessidade de pausas
while True:
    acender(leds[0], 30) #Acende o led vermelho
    acender(leds[2], 30) #Acende o led verde
    acender(leds[1], 4) #Acende o led amarelo
    #Após isso o ciclo se repete voltando a acender o led vermelho.
    print("CICLO_OK")