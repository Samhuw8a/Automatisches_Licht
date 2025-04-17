from __future__ import annotations
from nightlight.config import NightlightConfig
from nightlight._logging import logger
from gpiozero import DigitalInputDevice
import board
import adafruit_veml7700
import time


class Sensor:
    def is_triggered(self) -> bool:
        raise NotImplementedError()


class LightSensor(Sensor):
    def __init__(self, config: NightlightConfig) -> None:
        logger.debug("initialising I2C")
        i2c = board.I2C()
        logger.debug("creating the veml7700 driver")
        self.veml7700 = adafruit_veml7700.VEML7700(i2c)
        self.limit = config.light_limit

    def is_triggered(self) -> bool:
        lightlevel:int = self.veml7700.light
        logger.debug(f"Check if the veml7700 is above the limit got a value of: {lightlevel}.")
        return lightlevel < self.limit


class ClapSensor(Sensor):
    def __init__(self, pin: int = 24) -> None:
        logger.debug(f"initialising the soundsensor on pin: {pin}")
        self.digital_pin = DigitalInputDevice(pin, pull_up=False)

    def is_triggered(self) -> bool:
        logger.debug("cheking if the soundsensor Pin is active")
        return self.digital_pin.is_active


def main() -> int:
    config = NightlightConfig(led_count=164, timeout_time=10,
                              led_brightness=0.1, light_limit=1009)
    clap = ClapSensor()
    light = LightSensor(config)
    while True:
        print(clap.is_triggered())
        # print(light.is_triggered())
        time.sleep(0.1)


if __name__ == "__main__":
    raise SystemExit(main())
