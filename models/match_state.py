from enum import Enum

class MatchState(Enum):
    OPEN = "open"
    CANCELLED = "cancelled"
    COMPLETED = "completed"