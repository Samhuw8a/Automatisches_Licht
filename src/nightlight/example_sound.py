# -*- coding: iso-8859-1 -*-
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import DigitalInputDevice

# Erstelle den I2C-Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Erstelle das ADC-Objekt mit dem I2C-Bus
ads = ADS.ADS1115(i2c)

# Erstelle Single-Ended-Eing�nge auf den Kan�len
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

delayTime = 1
# Initialisiere den DigitalInputDevice fuer den Sensor an GPIO 24
digital_pin = DigitalInputDevice(
    24, pull_up=False
)  # pull_up=False, da pull_up_down=GPIO.PUD_OFF war

while True:
    analog = "%.2f" % chan0.voltage

    # Ausgabe auf die Konsole
    if not digital_pin.is_active:
        print(
            "Analoger Spannungswert:", analog, "V, ", "Grenzwert: noch nicht erreicht"
        )
    else:
        print("Analoger Spannungswert:", analog, "V, ", "Grenzwert: erreicht")
        print("---------------------------------------")

    # Reset + Delay
    time.sleep(delayTime)
