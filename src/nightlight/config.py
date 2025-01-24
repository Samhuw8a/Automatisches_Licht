from __future__ import annotations
from pydantic import BaseModel, validator
from yaml import safe_load
from pathlib import Path


class NightlightConfig(BaseModel):
    class Config:
        validate_assignment = True

    timeout_time: int  # Time for Timeout after activation in seconds

    @validator("timeout_time")
    @classmethod
    def is_correct_time(cls, timeout: int) -> int:
        if timeout < 0:
            raise ValueError(f"timeout_time must be a positve integer")
        return timeout


def load_config(path: str) -> NightlightConfig:
    with Path(path).open() as f:
        conf = safe_load(f)

    return NightlightConfig(timeout_time=conf["timeout_time"])
