from __future__ import annotations


class Sensor:
    def is_triggered(self) -> bool:
        raise NotImplementedError()


class LightSensor(Sensor):
    pass


class ClapSensor(Sensor):
    pass


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
