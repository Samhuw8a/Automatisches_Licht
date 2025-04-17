from __future__ import annotations
from time import sleep
from nightlight._logging import logger
from nightlight.config import load_config, NightlightConfig
from nightlight.light import Light
from nightlight.sensor import LightSensor, ClapSensor


def main() -> int:
    logger.info("Loading Config")
    config: NightlightConfig = load_config("config.yml")
    logger.info("initialising the RGB-Lightstrip driver")
    light: Light = Light(config)
    logger.info("initialising the VEML7700 LightSensor")
    light_sensor: LightSensor = LightSensor(config)
    logger.info("initialising the KY-037 SoundSensor")
    clap_sensor: ClapSensor = ClapSensor()
    sensorwait: float = config.sensorwait

    while True:
        clap_active: bool = clap_sensor.is_triggered()
        light_active: bool = light_sensor.is_triggered()
        logger.debug(f"Status: Light: {light_active}, Sound: {clap_active}")
        if clap_active and light_active:
            logger.info("Turning on the lights")
            light.enable()
            logger.debug(f"Sleeping for {config.timeout_time}")
            sleep(config.timeout_time)
            logger.info("Disabeling light")
            light.disable()
        sleep(sensorwait)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
