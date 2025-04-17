# -*- coding: iso-8859-1 -*-
import time
import board
import busio
from gpiozero import DigitalInputDevice

# Erstelle den I2C-Bus
delayTime = 1
# Initialisiere den DigitalInputDevice fuer den Sensor an GPIO 24
digital_pin = DigitalInputDevice(
    24, pull_up=False
)  # pull_up=False, da pull_up_down=GPIO.PUD_OFF war

while True:
    analog = "asdf"

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
