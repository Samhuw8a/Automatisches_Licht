from __future__ import annotations
from nightlight.config import NightlightConfig
from rpi_ws281x import Color, PixelStrip, ws


class Light:
    def __init__(self, config: NightlightConfig) -> None:
        led_strip = ws.SK6812_Strip_RGBW
        self.strip: PixelStrip = PixelStrip(
            config.led_count,
            config.led_pin,
            config.led_frequency,
            config.led_dma,
            config.led_invert,
            config.led_brightness,
            config.led_chanel,
            led_strip,
        )
        pass

    def enable(self) -> None:
        pass

    def disable(self) -> None:
        pass


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
