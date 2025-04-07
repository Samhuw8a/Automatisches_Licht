from __future__ import annotations
from nightlight.config import NightlightConfig
from gpiozero import DigitalInputDevice
import board
import adafruit_veml7700


class Sensor:
    def is_triggered(self) -> bool:
        raise NotImplementedError()


class LightSensor(Sensor):
    def __init__(self, pin: int, config: NightlightConfig) -> None:
        i2c = board.I2C()
        self.veml7700 = adafruit_veml7700.VEML7700(i2c)
        self.limit = config.light_limit

    def is_triggered(self) -> bool:
        return self.veml7700.light > self.limit


class ClapSensor(Sensor):
    def __init__(self, pin: int = 24) -> None:
        self.digital_pin = DigitalInputDevice(pin, pull_up=False)

    def is_triggered(self) -> bool:
        return self.digital_pin.is_activ


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
