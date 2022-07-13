from enum import Enum


class Direction(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


class InvalidDirection(Exception):
    pass
