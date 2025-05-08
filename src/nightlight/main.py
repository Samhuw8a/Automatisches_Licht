from __future__ import annotations
from time import sleep
from nightlight._logging import logger, verbal_conf, debug_conf
from nightlight.config import load_config, NightlightConfig
from nightlight.light import Light
from nightlight.sensor import LightSensor, ClapSensor
from argparse import ArgumentParser


def _init_argparser() -> ArgumentParser:
    parser = ArgumentParser(prog="nightlight")
    parser.add_argument(
        "-v", "--verbal", action="store_true", help="Print out information", dest="v"
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Print out more Debug information",
        dest="d",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="config.yml",
        dest="configpath",
        help="path to the config file default: config.yml",
    )
    return parser


def main(*argv: str) -> int:
    parser = _init_argparser()
    args = parser.parse_args(argv or None)
    if args.v:
        verbal_conf()
    elif args.d:
        debug_conf()

    logger.info("starting up...")
    logger.debug("Loading Config")
    config: NightlightConfig = load_config(args.configpath)
    logger.debug("initialising the RGB-Lightstrip driver")
    light: Light = Light(config)
    logger.debug("initialising the VEML7700 LightSensor")
    light_sensor: LightSensor = LightSensor(config)
    logger.debug("initialising the KY-037 SoundSensor")
    clap_sensor: ClapSensor = ClapSensor()
    sensorwait: float = config.sensorwait
    logger.info("finished Start-Up")

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
