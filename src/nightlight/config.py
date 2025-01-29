from __future__ import annotations
from pydantic import BaseModel, validator
from yaml import safe_load
from pathlib import Path


class NightlightConfig(BaseModel):
    class Config:
        validate_assignment = True

    timeout_time: int  # Time for Timeout after activation in seconds
    led_count: int
    led_pin: int
    led_frequency: int
    led_dma: int
    led_brightness: int
    led_invert: bool
    led_chanel: int

    @validator(
        "timeout_time", "led_count", "led_pin", "led_frequency", "led_dma", "led_chanel"
    )
    @classmethod
    def is_positiv(cls, value: int) -> int:
        if value < 0:
            raise ValueError("only positiv values are allowed")
        return value

    @validator("led_brightness")
    @classmethod
    def is_byte(cls, value: int) -> int:
        if value < 0 and value > 255:
            raise ValueError("only values between 0 and 255 are allowed")
        return value


def load_config(path: str) -> NightlightConfig:
    with Path(path).open() as f:
        conf = safe_load(f)

    return NightlightConfig(
        timeout_time=conf["timeout_time"],
        led_count=conf["led_count"],
        led_pin=conf["led_pin"],
        led_frequency=conf["led_frequency"],
        led_dma=conf["led_dma"],
        led_brightness=conf["led_brightness"],
        led_invert=conf["led_invert"],
        led_chanel=conf["led_chanel"],
    )
