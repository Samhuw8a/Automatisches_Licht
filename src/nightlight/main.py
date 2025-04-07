from __future__ import annotations
from time import sleep
from nightlight._logging import logger
from nightlight.config import load_config, NightlightConfig
from nightlight.light import Light
from nightlight.sensor import LightSensor, ClapSensor


def main() -> int:
    logger.info("Loading Config")
    config: NightlightConfig = load_config("config.yml")
    light: Light = Light(config)
    light_sensor: LightSensor = LightSensor()
    clap_sensor: ClapSensor = ClapSensor()

    while True:
        if clap_sensor.is_triggered() and light_sensor.is_triggered():
            logger.info("Enableing light")
            light.enable()
            logger.debug(f"Sleeping for {config.timeout_time}")
            sleep(config.timeout_time)
            logger.info("Disabeling light")
            light.disable()
        sleep(0.1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
