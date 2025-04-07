from __future__ import annotations
from nightlight.config import NightlightConfig
from rpi5_ws2812 import Color, WS2812SpiDriver


class Light:
    def __init__(self, config: NightlightConfig) -> None:
        self.strip = WS2812SpiDriver(spi_bus=0, led_count=config.led_count)
        self.strip.set_brightness(config.led_brightness)
        self.white: Color = Color(255, 255, 255)

    def enable(self) -> None:
        self.strip.set_all_pixels(self.white)
        self.strip.show()

    def disable(self) -> None:
        self.strip.clear()


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
