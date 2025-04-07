from __future__ import annotations
from pydantic import BaseModel, validator
from yaml import safe_load
from pathlib import Path


class NightlightConfig(BaseModel):
    class Config:
        validate_assignment = True

    timeout_time: int  # Time for Timeout after activation in seconds
    led_count: int
    led_brightness: int
    light_limit:int

    @validator(
        "timeout_time", "led_count", "light_limit"
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
        led_brightness=conf["led_brightness"],
        light_limit=conf["light_limit"],
    )
