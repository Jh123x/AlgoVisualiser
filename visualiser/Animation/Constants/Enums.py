import enum

class State(enum.Enum):
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2
    BLOCKED = 3
    SOURCE = 4
    TARGET = 5