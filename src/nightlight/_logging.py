import logging.config

logging_config: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        },
        "non_verbal": {"format": "%(message)s"},
        "debug": {"format": "%(asctime)s: %(levelname)s: %(message)s"},
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {"root": {"level": "WARNING", "handlers": ["stdout"]}},
}

logging.config.dictConfig(config=logging_config)
logger = logging.getLogger("nightlight")


def verbal_conf() -> None:
    logging_config["loggers"]["root"]["level"] = "INFO"
    logging_config["handlers"]["stdout"]["formatter"] = "non_verbal"
    logging.config.dictConfig(config=logging_config)


def debug_conf() -> None:
    logging_config["loggers"]["root"]["level"] = "DEBUG"
    logging_config["handlers"]["stdout"]["formatter"] = "debug"
    logging.config.dictConfig(config=logging_config)
