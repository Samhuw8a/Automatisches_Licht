from __future__ import annotations
from nightlight.config import NightlightConfig
from nightlight._logging import logger
import time
from rpi5_ws2812.ws2812 import Color, WS2812SpiDriver


class Light:
    def __init__(self, config: NightlightConfig) -> None:
        logger.debug("Creating a WS2812SpiDriver instance on spi_bus 0 with spi_device 0")
        self.strip = WS2812SpiDriver(
            spi_bus=0, spi_device=0, led_count=config.led_count).get_strip()
        logger.debug(f"setting the brightness to {config.led_brightness}")
        self.strip.set_brightness(config.led_brightness)
        self.white: Color = Color(255, 255, 255)

    def enable(self) -> None:
        logger.debug("turning all Pixels to white")
        self.strip.set_all_pixels(self.white)
        logger.debug("pushing the changes to the strip")
        self.strip.show()

    def disable(self) -> None:
        logger.debug("clearing all the Pixel")
        self.strip.clear()


def main() -> int:
    config = NightlightConfig(led_count=164, timeout_time=10,
                              led_brightness=0.1, light_limit=69)
    l = Light(config)
    l.enable()
    time.sleep(5)
    l.disable()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
